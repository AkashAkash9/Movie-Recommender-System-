import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load data
@st.cache_data
def load_data():
    movies = pd.read_csv("movies.csv")
    ratings = pd.read_csv("ratings.csv")
    data = pd.merge(ratings, movies, on='movieId')
    user_movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')
    movie_user_matrix = user_movie_matrix.fillna(0)
    movie_user_matrix_T = movie_user_matrix.T
    cosine_sim = cosine_similarity(movie_user_matrix_T)
    similarity_df = pd.DataFrame(cosine_sim, index=movie_user_matrix_T.index, columns=movie_user_matrix_T.index)
    return similarity_df

similarity_df = load_data()

# Recommender function
def recommend_movies(movie_name, top_n=5):
    if movie_name not in similarity_df:
        return []
    sim_scores = similarity_df[movie_name].sort_values(ascending=False)
    return sim_scores[1:top_n+1]

# Streamlit UI
st.title("🎬 Movie Recommender System")
st.write("Select a movie to get top similar recommendations based on user ratings.")

movie_list = list(similarity_df.columns)
selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend"):
    st.subheader("Top Recommendations:")
    results = recommend_movies(selected_movie)
    for i, (title, score) in enumerate(results.items(), start=1):
        st.write(f"{i}. **{title}** — Similarity Score: `{score:.2f}`")
