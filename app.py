import streamlit as st
import pandas as pd
import ast

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.title("🎬 Movie Recommender")
st.write("Choose a genre and discover recommended movies.")
st.info("This app recommends movies by genre using movie metadata.")

MOVIES_FILE = r"C:\YeJunHan\movie-recommender\movies_metadata.csv"


def extract_genres(text):
    try:
        genres = ast.literal_eval(text)
        if isinstance(genres, list):
            return [g["name"] for g in genres if "name" in g]
        return []
    except:
        return []


@st.cache_data
def load_data():
    movies = pd.read_csv(MOVIES_FILE, low_memory=False)

    # 필요한 컬럼만 사용
    movies = movies[["title", "overview", "genres", "vote_average", "release_date"]].copy()

    # 타입 정리
    movies["title"] = movies["title"].fillna("").astype(str)
    movies["overview"] = movies["overview"].fillna("").astype(str)
    movies["genres"] = movies["genres"].fillna("").astype(str)
    movies["release_date"] = movies["release_date"].fillna("Unknown").astype(str)
    movies["vote_average"] = pd.to_numeric(movies["vote_average"], errors="coerce").fillna(0)

    # 장르 파싱
    movies["genre_list"] = movies["genres"].apply(extract_genres)

    # 필터링
    movies = movies[movies["title"].str.len() > 1]
    movies = movies[movies["overview"].str.len() > 20]
    movies = movies[movies["genre_list"].map(len) > 0]

    # 너무 이상한 제목 제거용 최소 정리
    movies = movies[~movies["title"].str.startswith("#")]
    movies = movies[~movies["title"].str.startswith("$")]

    # 중복 제거
    movies = movies.drop_duplicates(subset="title")
    movies = movies.reset_index(drop=True)

    return movies


movies = load_data()

st.caption(f"Dataset size: {len(movies)} movies")

# 전체 장르 목록 만들기
all_genres = sorted({genre for sublist in movies["genre_list"] for genre in sublist})

selected_genre = st.selectbox("Choose a genre", all_genres)
min_rating = st.slider("Minimum rating", 0.0, 10.0, 5.0, 0.5)
num_results = st.slider("Number of recommendations", 3, 15, 8)


def recommend_by_genre(dataframe, genre, min_rating_value, n):
    filtered = dataframe[
        dataframe["genre_list"].apply(lambda genres: genre in genres)
    ].copy()

    filtered = filtered[filtered["vote_average"] >= min_rating_value]

    filtered = filtered.sort_values(
        by=["vote_average", "release_date"],
        ascending=[False, False]
    )

    return filtered.head(n)


if st.button("Get Recommendations"):
    results = recommend_by_genre(movies, selected_genre, min_rating, num_results)

    if results.empty:
        st.warning("No movies found for this genre and rating combination.")
    else:
        st.subheader(f"Top {len(results)} movies in '{selected_genre}'")

        for _, row in results.iterrows():
            genres_text = ", ".join(row["genre_list"])

            with st.container():
                st.markdown(f"### {row['title']}")
                st.write(f"**Genres:** {genres_text}")
                st.write(f"**Release date:** {row['release_date']}")
                st.write(f"**Average rating:** {row['vote_average']}")
                st.write(row["overview"])
                st.markdown("---")