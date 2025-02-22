# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load interview data (assuming a CSV format for simplicity)
interviews = pd.read_csv("../data/interview_transcripts.txt", delimiter="\t")

# Example: Using count vectorizer to find common themes
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(interviews['Transcript'])

# Calculate cosine similarity to identify similar themes
cos_sim = cosine_similarity(X)

# Output the cosine similarity matrix
print(cos_sim)
