from time import sleep
import pandas as pd
import os
import pickle
import requests
import random

df = pickle.load(open("Pickle Files/df_with_image_url.pkl", "rb"))


def get_url(name):
    x = requests.get("https://api.jikan.moe/v4/anime?q=" + str(name) + "&sfw").json()
    sleep(random.uniform(0.5, 0.7))
    for i in range(len(x['data'])):
        if x['data'][i]['title'] == name:
            print(df[df['Name'] == name].index[0], " : ", name)
            return x['data'][i]['images']['jpg']['image_url']


x = []
for i in df['Name']:
    x.append(get_url(i))

df["img_url"] = pd.DataFrame(x)

pickle.dump(df, open("Pickle Files/img_url.pkl", "wb"))
