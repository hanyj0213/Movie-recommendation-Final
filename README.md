# 🎬 Movie Recommendation System

This project is a minimum viable data product developed for the Minor Data-Driven Decision Making individual assignment.

The application recommends movies based on genre and minimum rating using a real-world movie metadata dataset.

## Project Goal

The goal of this project is to explore data-driven decision making by building a simple and usable recommendation system.

The project focuses on:
- Data cleaning
- Genre processing
- Recommendation logic
- MVP development
- Iterative improvement
- User experience

## Learning Inspiration

This project was inspired by two selected videos:

- AI Python for Beginners
- Become a Data Storyteller with Streamlit

These videos helped me understand how Python can be used to build simple data applications and how Streamlit can turn data into an interactive user experience.

## Features

- Genre-based movie recommendations
- Minimum rating filter
- Clean Streamlit interface
- Real-world movie metadata
- Data preprocessing and filtering
- Notebook with explanation and insights

## Technologies Used

- Python
- Pandas
- Streamlit
- Jupyter Notebook

## Dataset

The dataset is not included in this repository because it is too large.

Download the dataset here:

https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset

Required file:
```
movies_metadata.csv
```

After downloading, place movies_metadata.csv in the main project folder.

## Project Structure
```
Movie-recommendation-Final/
│
├── movie_recommendation_YeJun_Han.ipynb   # Main notebook with code, markdown, and insights
├── app.py                                 # Streamlit recommendation app
├── README.md                              # Instructions and project explanation
├── requirements.txt                       # Required Python libraries
└── movies_metadata.csv
```
## Installation

Install the required libraries:
```
pip install -r requirements.txt
```
Contents of requirements.txt:

pandas
streamlit
notebook

If needed, install them manually:
```
pip install pandas streamlit notebook
```
## How to Run the Notebook

The notebook is the main submitted code file.

Open it with Jupyter Notebook:
```
jupyter notebook movie_recommendation_YeJun_Han.ipynb
```
Run all cells from top to bottom.

## The notebook includes:

Project introduction
Video inspiration
Dataset loading
Data cleaning
Genre processing
Recommendation logic
Example output
Reflection and insights


## How to Run the Streamlit App

Make sure movies_metadata.csv is in the same folder as app.py.

Then run:

```
streamlit run app.py
or
python -m streamlit run app.py
or
py -m streamlit run app.py
```

The app will open in your browser.

If it does not open automatically, copy the local URL from the terminal and paste it into your browser.

## How to Use the App

Once the Streamlit app opens:

1. Choose a movie genre from the dropdown menu
2. Select a minimum rating
3. Click the recommendation button
4. View the recommended movies

## Iteration Process

### Iteration 1

The first version used raw movie data.
The system worked, but the movie selection contained noisy and unclear titles.

### Iteration 2

The second version worked technically, but the user experience was still poor because users had to choose from a long and unclear movie title list.

### Iteration 3

The final version switched to genre-based recommendations.
This improved usability, made the interface cleaner, and created a more stable recommendation experience.

## Key Learnings

Through this project, I learned that:

Data quality is critical for building reliable applications
A technically working system is not enough if the user experience is poor
Simpler solutions can be more effective than complex models
Iteration is important in MVP development
Streamlit is useful for quickly building interactive data products

## Troubleshooting

If the notebook or app does not work, check the following:

movies_metadata.csv is placed in the main project folder
The filename is exactly movies_metadata.csv
Required libraries are installed
The notebook or app is run from the correct folder


## Author

Han Yejun



