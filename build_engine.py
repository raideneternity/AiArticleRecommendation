import pandas as pd
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# 1. Load Model
try:
    model = SentenceTransformer('my_fyp_model')
    print("Loaded custom trained model.")
except:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Warning: Custom model not found. Using base model.")

# 2. Load Articles
df = pd.read_csv('articles.csv')
print(f"Loaded {len(df)} articles.")

# 🛠️ FIX: Fill empty values with empty strings to prevent "Float" error
df['title'] = df['title'].fillna("No Title").astype(str)
df['content'] = df['content'].fillna("").astype(str)

# 3. Create Vectors (Embeddings)
print("Converting articles to vectors...")
# Combine Title + Content for the AI to read
article_texts = (df['title'] + ". " + df['content']).tolist()

# normalize_embeddings=True makes the Match Score accurate (0-100%)
embeddings = model.encode(article_texts, normalize_embeddings=True)

# 4. Build FAISS Index
dimension = embeddings.shape[1]
# Use IndexFlatIP (Inner Product) for Cosine Similarity
index = faiss.IndexFlatIP(dimension) 
index.add(embeddings)

# 5. Save everything
with open('fyp_search_index.faiss', 'wb') as f:
    pickle.dump(index, f)

# Save raw data (including Category)
with open('fyp_articles_data.pkl', 'wb') as f:
    pickle.dump(df.to_dict('records'), f)

print("Search engine built! Saved 'fyp_search_index.faiss' and 'fyp_articles_data.pkl'")