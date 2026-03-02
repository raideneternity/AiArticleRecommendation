import pandas as pd
from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader

# 1. Load Data
print("Loading data...")
goals_df = pd.read_csv('goals.csv')
articles_df = pd.read_csv('articles.csv')

# Create a dictionary for fast article lookups
# Format: {1: "Title. Content...", 2: "Title. Content..."}
articles_dict = {}
for index, row in articles_df.iterrows():
    # Combine Title + Content for context
    articles_dict[row['id']] = f"{row['title']}. {row['content']}"

# 2. Prepare Training Examples
print("Preparing training pairs...")
train_examples = []
for index, row in goals_df.iterrows():
    # 🟢 NEW: Combine Goal Title + Description
    goal_text = f"{row['title']}. {row['description']}"
    article_id = row['article_id']
    
    # Get the matching article text
    if article_id in articles_dict:
        article_text = articles_dict[article_id]
        # Create a "Positive Pair"
        train_examples.append(InputExample(texts=[goal_text, article_text], label=1.0))

# 3. Initialize the Model
model_name = 'all-MiniLM-L6-v2'
model = SentenceTransformer(model_name)

# 4. Setup Training
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)
train_loss = losses.CosineSimilarityLoss(model)

# 5. Train (Fine-Tune)
print("Training model... (This creates the brain connection between Goals and Articles)")
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=1, warmup_steps=100)

# 6. Save
model.save('my_fyp_model')
print("Training complete! Model saved to 'my_fyp_model' folder.")