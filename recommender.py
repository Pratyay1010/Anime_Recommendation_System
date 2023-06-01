import pickle
import numpy as np

anime_names_pt = pickle.load(open("Pickle Files/anime_names_pt.pkl", "rb"))
df = pickle.load(open("Pickle Files/img_url.pkl", "rb"))
similarity_collaborative_based = pickle.load(open("Pickle Files/similarity_collaborative_based.pkl", "rb"))
similarity_content_based = pickle.load(open("Pickle Files/similarity_content_based.pkl", "rb"))


def recommend_anime_context_based(name):
    index = df[df['Name'] == name].index[0]
    similar_anime = sorted(list(enumerate(similarity_content_based[index])), key=lambda x: x[1], reverse=True)[1:51]

    return similar_anime


def recommend_anime_collaborative_based(name):
    index = np.where(anime_names_pt == name)[0][0]
    similar_anime = sorted(list(enumerate(similarity_collaborative_based[index])), key=lambda x: x[1], reverse=True)[
                    1:51]

    return similar_anime


def recommend_anime_hybrid_based(name):
    content_based_recommendations = recommend_anime_context_based(name)
    collaborative_based_recommendations = recommend_anime_collaborative_based(name)

    x = []
    for i in range(len(content_based_recommendations)):
        temp = content_based_recommendations[i]
        x.append((temp[0], temp[1] * 1.6, "1"))

    for i in range(len(collaborative_based_recommendations)):
        temp = collaborative_based_recommendations[i]
        x.append((temp[0], temp[1] * 0.7, "2"))

    x = sorted(x, key=lambda x: x[1], reverse=True)[0:15]

    recommended_list = []
    for i in x:
        if i[2] == '1':
            recommended_list.append(df['Name'][i[0]])
        else:
            recommended_list.append(anime_names_pt[i[0]])

    return recommended_list
