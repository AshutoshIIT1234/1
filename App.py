import pickle
import streamlit as st
import requests
import pandas as pd
Anime_dict=pickle.load(open('Model\Anime_list.pkl', 'rb'))
Anime=pd.DataFrame(Anime_dict)
st.title('Anime Recommender System')
selected_Anime_name=st.selectbox(
    'Select a Anime',
    Anime['Name'].values
)
similarity=pickle.load(open('Model\similarity.pkl', 'rb'))
def recommend_Anime(selected_Anime_name):
    index=Anime[Anime['Name']==selected_Anime_name].index[0]
    distances=similarity[index]
    Anime_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_Anime=[]
    for i in Anime_list:
        recommended_Anime.append(Anime.iloc[i[0]].Name)
    return recommended_Anime

if st.button('Show Recommendation'):
    recommendations=recommend_Anime(selected_Anime_name)
    for i in recommendations:
        st.write(i)