# A Content-Based Movie Recommender System

A Movie Recommendation System built using Machine Learning and Streamlit that recommends movies similar to the user's selected movie.

## Live Demo

🔗https://content-based-movie-recommender-system-mcwkhfbgwqipaynep9whfy.streamlit.app/

## Features
- Recommend top 5 similar movies
- Fetch movie posters using TMDB API
- Interactive Streamlit web interface
- Content-based filtering using cosine similarity
- Real-time recommendations

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- TMDB API
- Pickle

## Dataset
TMDB 5000 Movie Dataset

Dataset contains:
- Movie titles
- Genres
- Keywords
- Cast
- Crew
- Overview

## Project Workflow
1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Text Vectorization
5. Cosine Similarity Calculation
6. Recommendation Generation
7. Streamlit Web App Deployment


## Screenshots

## 📸 Screenshots

### Home Page
<img src="images/home_page.png" width="900">

### Recommendation Results
<img src="images/recommendations.png" width="900">

## Installation

Clone repository
```bash
git clone https://github.com/yourusername/content-based-movie-recommender-system.git
```

Move into project folder
```bash
cd content-based-movie-recommender-system
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run app
```bash
streamlit run app.py
```

## Acknowledgement
This project was developed by following and learning from the CampusX Movie Recommender System tutorial. I implemented the code, customized the UI, deployed the application using Streamlit Community Cloud, and made modifications to improve the user experience.
Special thanks to CampusX for the educational content.
