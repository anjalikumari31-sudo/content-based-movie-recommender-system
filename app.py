#using streamlit , we can use flask
import streamlit as st
import pickle
import pandas as pd
import requests # it hits the api and get poster id


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

st.title('Movie Recommender System')

# Movie selection box
selected_movies_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

# Display selected movie
st.write(f"You selected: {selected_movies_name}")

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



