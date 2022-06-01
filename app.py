import streamlit as st
import pickle
import pandas as pd
import requests

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=62092dc3c593e864c7b3d8fce24cb4c1language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # to get index of movie
    distances = similarity[movie_index]  # to calculate similarity
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recomended_movies=[]
    for i in movies_list:
        movie_id = i[0]
        #fetch poster from API
        recomended_movies.append(movies.iloc[i[0]].title)
        # recomended_movies_posters.append(fetch_poster(movie_id))
    return recomended_movies

movies_list = pickle.load(open('movies.pkl','rb'))
movies= pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie = st.selectbox(
    'Please select the movie!',
movies['title'].values
)
if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
    # col1,col2,col3,col4,col5 = st.beta_columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])