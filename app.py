import streamlit as st
import pickle
import numpy as np

def recommend(anime_name):
    index = np.where(anime_pt.index==anime_name)[0][0]
    r = sorted(list(enumerate(similarity[index])), key= lambda x:x[1], reverse=True)[1:6]

    recomendation=[]
    for i in r:
        recomendation.append(anime_pt.index[i[0]])

    return  recomendation



anime_pt = pickle.load(open("anime_pivot_table.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))


st.title("Anime Recommendation System")

option = st.selectbox(
    'Select an Anime',
    (anime_pt.index))

if st.button('Recommend'):
    recomendation = recommend(option)

    for i in recomendation:
        st.write(i)