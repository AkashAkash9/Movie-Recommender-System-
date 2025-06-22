# 🎬 Movie Recommender System

A simple and effective movie recommendation system built using **collaborative filtering** on the MovieLens dataset. This app recommends movies based on user rating similarities and is deployed using **Streamlit** for interactive usage.

## 🚀 Features

- Select any movie from the dropdown
- Get top similar movie recommendations based on user rating behavior
- Lightweight and fast (no model training required)
- Deployable via Streamlit locally or on Streamlit Cloud

## 🧠 How It Works

This system uses **cosine similarity** on a **user-movie rating matrix** to identify which movies have similar rating patterns. It is a pure collaborative filtering approach (no genres or metadata used).

## 🗂️ Dataset

We use the [MovieLens 100k dataset](https://grouplens.org/datasets/movielens/):

- `movies.csv` — movie ID, title, genres  
- `ratings.csv` — user ratings on a 0–5 scale

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit

## 💻 How to Run Locally

1. **Clone the repository**
git clone https://github.com/your-username/movie-recommender-system-.git
cd movie-recommender-system-

3. **Create and activate a virtual environment (optional but recommended)**
python -m venv venv
venv\Scripts\activate    # on Windows

4. **Run the app**
streamlit run app.py

## 📁 Project Structure

movie-recommender/
├── app.py              # Streamlit app
├── movies.csv          # Movie metadata
├── ratings.csv         # User ratings
├── requirements.txt    # Python dependencies
└── README.md           # This file

## 📸 Demo Video link: https://drive.google.com/file/d/1M471IbvrwkhRPB71gf0mevul7rAkA5ov/view?usp=sharing

## ✨ Future Improvements
Add content-based filtering using genres and tags

Combine with deep learning for hybrid recommendations

Save computed similarity matrix to .pkl for faster loading

## 📬 Contact
LinkedIN: https://www.linkedin.com/in/akash-rajput-1a25b52a0/
Feel free to fork, star, and contribute!

