import pickle
import streamlit as st
import requests
import pandas as pd
movie_dict=pickle.load(open('Model\movie_list.pkl', 'rb'))
movies=pd.DataFrame(movie_dict)
st.title('Movie Recommender System')
selected_movie_name=st.selectbox(
    'Select a movie',
    movies['title'].values
)
similarity=pickle.load(open('Model\similarity.pkl', 'rb'))
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommend_movie(selected_movie_name):
    movie_index=movies[movies['title'] == selected_movie_name].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommend_movie_poster=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommend_movie_poster.append(fetch_poster(movies.iloc[i[0]]['id']))
    return recommended_movies, recommend_movie_poster

if st.button('Show Recommendation'):
    # import the recommendation function

    recommended_movies,recommend_movie_poster=recommend_movie(selected_movie_name)
    st.write('Recommended Movies')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommend_movie_poster[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommend_movie_poster[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommend_movie_poster[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommend_movie_poster[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommend_movie_poster[4])
    

    
