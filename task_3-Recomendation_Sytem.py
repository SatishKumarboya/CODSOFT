import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Expanded movie dataset with multiple genres
data = {
    'movie_id': list(range(1, 21)),
    'title': [
        'The Dark Knight', 'Inception', 'Interstellar', 'Avengers: Endgame',
        'Pride and Prejudice', 'The Notebook', 'The Godfather',
        'Pulp Fiction', 'The Lion King', 'Frozen',
        'Get Out', 'Hereditary', 'Parasite', 'Knives Out',
        'Harry Potter and the Sorcerer\'s Stone', 'The Lord of the Rings: Fellowship of the Ring',
        'Spirited Away', 'Coco', 'The Conjuring', 'Joker'
    ],
    'genres': [
        'Action Crime Drama',
        'Action Sci-Fi Thriller',
        'Adventure Drama Sci-Fi',
        'Action Adventure Sci-Fi',
        'Romance Drama',
        'Romance Drama',
        'Crime Drama',
        'Crime Drama',
        'Animation Adventure Drama',
        'Animation Adventure Comedy',
        'Horror Mystery Thriller',
        'Horror Drama Mystery',
        'Thriller Drama',
        'Mystery Comedy Drama',
        'Fantasy Adventure Family',
        'Fantasy Adventure Action',
        'Animation Fantasy Adventure',
        'Animation Family Fantasy',
        'Horror Mystery Supernatural',
        'Crime Drama Thriller'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("🎬 Available Movies in Database:\n")
print(df[['title', 'genres']], "\n")

# Vectorize genres
count_vectorizer = CountVectorizer()
genre_matrix = count_vectorizer.fit_transform(df['genres'])

# Recommendation function
def recommend_movies(preferred_genres, top_n=5):
    user_vec = count_vectorizer.transform([preferred_genres])
    cosine_similarities = cosine_similarity(user_vec, genre_matrix).flatten()
    recommended_indices = cosine_similarities.argsort()[-top_n:][::-1]
    
    print("\n✅ Top Recommended Movies for You:")
    for idx in recommended_indices:
        print(f"- {df.iloc[idx]['title']} (Genres: {df.iloc[idx]['genres']})")
    print("\n")

# Main loop for user input
print("🎁 Example genres you can enter: Action Sci-Fi, Romance Drama, Horror Thriller, Animation Family Fantasy, Mystery Drama")

while True:
    user_input = input("\n👉 Enter your preferred genres (or type 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        print("👋 Thank you for using the Movie Recommendation System. Goodbye!")
        break
    elif user_input == "":
        print("⚠️ Please enter valid genres or type 'exit' to quit.")
    else:
        recommend_movies(user_input)
