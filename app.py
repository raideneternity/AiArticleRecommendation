from flask import Flask, request, jsonify
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import os

app = Flask(__name__)

print("Starting server...")

# 1. Load Model
try:
    model = SentenceTransformer('my_fyp_model')
except:
    model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Load Database
with open('fyp_search_index.faiss', 'rb') as f:
    index = pickle.load(f)
with open('fyp_articles_data.pkl', 'rb') as f:
    articles = pickle.load(f)

print("✅ Server Ready!")

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get User Input
        data = request.json
        user_goal = data.get('goal', '')
        
        if not user_goal:
            return jsonify([])

        # 1. Convert goal to vector (Normalize it too!)
        vector = model.encode([user_goal], normalize_embeddings=True)
        
        # 2. Search for top 10 matches (k=10)
        # distances = similarity score (higher is better for Inner Product)
        # indices = the ID of the article in the list
        k = 10
        distances, indices = index.search(vector, k)
        
        # 3. Format Results
        results = []
        # indices[0] is the list of top 10 article IDs
        # distances[0] is the list of top 10 scores
        for i in range(len(indices[0])):
            idx = int(indices[0][i])
            score = float(distances[0][i]) # 0.85, 0.92, etc.
            
            if idx < len(articles):
                article_data = articles[idx]
                
                # Convert 0.85 -> 85.0%
                match_percentage = round(score * 100, 1)

                results.append({
                    "title": article_data['title'],
                    "category": article_data['category'], # 🟢 Added Category
                    "content": article_data['content'],
                    "match_score": match_percentage # 🟢 Added Score
                })
                
        return jsonify(results)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)