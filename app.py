import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import pickle
import recommender


st.set_page_config(layout="wide")

df = pickle.load(open("Pickle Files/img_url.pkl", "rb"))

st.markdown(
    """
    <h1 style='text-align: center; color: yellow;'>Anime Recommendation System</h1>
    """,
    unsafe_allow_html=True
)


option = st.selectbox(
    'Choice your Anime',
    df['Name'])

if st.button('Recommend'):

    recommend_anime = recommender.recommend_anime_hybrid_based(option)

    img_list = {}

    st.header('Recommended Anime')
    for name in recommend_anime:
        index = df[df['Name'] == name].index[0]
        img_list[name] = df['img_url'][index]

    image_width = 200
    image_height = 300

    cols = st.columns(5)

    num_images = 10

    for i, (name, url) in enumerate(img_list.items()):
        flag = 0
        # Check if the image URL exists
        if url is None:
            # Display a white image
            white_image = Image.new('RGB', (image_width, image_height), (255, 255, 255))
            with cols[i % 5]:
                st.image(white_image, width=image_width)
                st.write(name)
        else:
            response = requests.get(url)
            if response.status_code == 200:
                # Display the image
                image = Image.open(BytesIO(response.content))
                with cols[i % 5]:
                    st.image(image, width=image_width)
                    st.write(name)
            else:
                # Display a white image
                white_image = Image.new('RGB', (image_width, image_height), (255, 255, 255))
                with cols[i % 5]:
                    st.image(white_image, width=image_width)
                    st.write(name)

        # Break the loop if the desired number of images is reached
        if i + 1 == num_images:
            break

    img_list = {}
