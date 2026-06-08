#using streamlit , we can use flask
import streamlit as st
import pickle
import pandas as pd
import requests # it hits the api and get poster id

st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* Main container */
.block-container {
    max-width: 1000px;
    padding-top: 2rem;
}

/* Title */
h1 {
    text-align: center;
    font-size: 3rem !important;
    color: white;
    margin-bottom: 0;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #b0b0b0;
    margin-bottom: 40px;
}

/* Dropdown box */
div[data-baseweb="select"] > div {
    min-height: 48px;
    font-size: 16px;
    border-radius: 10px;
}

/* Dropdown selected text */
div[data-baseweb="select"] span {
    font-size: 16px;
}

/* Select Movie heading */
.select-heading {
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 12px;
}

/* Recommend button */
.stButton > button {
    width: 180px;
    height: 48px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: 600;
    color:white;
}

/* Movie names */
.movie-title {
    text-align: center;
    font-size: 15px;
    font-weight: 600;
    margin-top: 10px;
    min-height: 45px;
}

</style>
""", unsafe_allow_html=True)


API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

session = requests.Session()

def fetch_poster(movie_id):
    url = (
        f"https://api.themoviedb.org/3/movie/"
        f"{movie_id}?api_key={API_KEY}&language=en-US"
    )

    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

        return "https://via.placeholder.com/300x450?text=No+Poster"

    except Exception as e:
        print(f"Error for {movie_id}: {e}")
        return "https://via.placeholder.com/300x450?text=Poster+Unavailable"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
         #fetching the poster tmdb API
         #st.write(movies.iloc[i[0]].title)
         recommended_movies.append(movies.iloc[i[0]].title)
         recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.markdown("""
<h1>🎬 Movie Recommender System</h1>
<p style='text-align:center;font-size:20px;'>
Discover movies similar to your favorites
</p>
""", unsafe_allow_html=True)

# Movie selection box
st.markdown(
    "<div class='select-heading'>🎬 Select a Movie</div>",
    unsafe_allow_html=True
)

selected_movies_name = st.selectbox(
    "",
    movies['title'].values,
    label_visibility="collapsed"
)

# Display selected movie
st.info(f"Selected Movie: {selected_movies_name}")

#make a bottom to show recommend and on clicking best 5 movies will be recommended to user
if st.button("Recommend"):
   names,poster= recommend(selected_movies_name)
   col1,col2,col3,col4,col5= st.columns(5)
   with col1:
       st.text(names[0])
       if poster[0]:
           st.image(poster[0])


   with col2:
       st.text(names[1])
       if poster[1]:
           st.image(poster[1])


   with col3:
       st.text(names[2])
       if poster[2]:
           st.image(poster[2])


   with col4:
       st.text(names[3])
       if poster[3]:
           st.image(poster[3])


   with col5:
       st.text(names[4])
       if poster[4]:
           st.image(poster[4])



