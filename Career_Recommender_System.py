import nltk
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

career_df = pd.read_csv('/Users/sella/Downloads/field_vs_occupation_dataset.csv')

# Ordinal encoding for Education Level
education_mapping = {
    'High School': 0,
    'Bachelor\'s': 1,
    'Master\'s': 2,
    'PhD': 3
}
career_df['Education Level Encoded'] = career_df['Education Level'].map(education_mapping)

# Replace original column with the encoded
career_df = career_df.drop('Education Level', axis=1)
career_df = career_df.rename(columns={'Education Level Encoded': 'Education Level'})

# Feature selection (no job security, skills gap, career events, or family influence)
numerical_features = [
    'Age', 'Years of Experience', 'Job Satisfaction',
    'Work-Life Balance', 'Salary', 'Job Opportunities',
    'Professional Networks', 'Technology Adoption', 'Education Level'
]

binary_features = [
    'Mentorship Available', 'Certifications', 'Freelancing Experience',
    'Geographic Mobility', 'Career Change Interest'
]

features = numerical_features + binary_features

# Scale data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(career_df[features])
scaled_df = pd.DataFrame(scaled_data, columns=features)

# KMeans -- collaborative filtering
kmeans = KMeans(n_clusters=5, random_state=42)
career_df['Cluster'] = kmeans.fit_predict(scaled_df)


# TF-IDF -- content-based filtering
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(career_df['Current Occupation'])

# Hybrid Recommender
def hybrid_recommender(user_input, df, scaled_df, scaler, kmeans_model, tfidf_matrix, alpha=0.5, top_n=3):
    # Convert input dict to vector (numerical + binary features)
    user_vector = np.array([user_input[feat] for feat in features]).reshape(1, -1)
    #user_scaled = scaler.transform(user_vector)
    user_scaled = scaler.transform(pd.DataFrame(user_vector, columns=features))


    # Content-Based: Cosine similarity (between user and current occupation)
    similarities = cosine_similarity(user_scaled, scaled_df).flatten()
    top_sim_indices = similarities.argsort()[::-1][:20]  # Get top 20 similar users
    content_careers = df.iloc[top_sim_indices]['Current Occupation']

    content_scores = Counter(content_careers)
    # Normalize content-based scores
    for k in content_scores:
        content_scores[k] /= len(top_sim_indices)

    # Collaborative: KMeans cluster matching (predict user's cluster based on their info)
    cluster_label = kmeans_model.predict(user_scaled)[0]
    cluster_peers = df[df['Cluster'] == cluster_label]['Current Occupation']

    collab_scores = Counter(cluster_peers)
    total = sum(collab_scores.values())
    for k in collab_scores:
        collab_scores[k] /= total

    # Combine content-based and collaborative scores
    hybrid_scores = {}
    for career in set(content_scores.keys()).union(collab_scores.keys()):
        hybrid_scores[career] = (
                alpha * content_scores.get(career, 0) +
                (1 - alpha) * collab_scores.get(career, 0)
        )

    # Return top 3 recommendation
    recommended = sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return [career for career, score in recommended]


# Get User Input

def get_user_input():
    print("Please enter the following values:")

    user_input = {}

    # Get numerical inputs
    user_input['Age'] = int(input("Age: "))
    user_input['Years of Experience'] = int(input("Years of Experience: "))
    user_input['Job Satisfaction'] = int(input("Job Satisfaction (1-10): "))
    user_input['Work-Life Balance'] = int(input("Work-Life Balance (1-10): "))
    user_input['Salary'] = int(input("Salary: "))
    user_input['Job Opportunities'] = int(input("Job Opportunities: "))
    user_input['Professional Networks'] = int(input("Professional Networks (1-10): "))
    user_input['Technology Adoption'] = int(input("Technology Adoption (1-10): "))

    # Get binary inputs
    user_input['Education Level'] = int(input("Education Level (0: High School, 1: Bachelor's, 2: Master's, 3: PhD): "))
    user_input['Mentorship Available'] = int(input("Mentorship Available (1 for Yes, 0 for No): "))
    user_input['Certifications'] = int(input("Certifications (1 for Yes, 0 for No): "))
    user_input['Freelancing Experience'] = int(input("Freelancing Experience (1 for Yes, 0 for No): "))
    user_input['Geographic Mobility'] = int(input("Geographic Mobility (1 for Yes, 0 for No): "))
    user_input['Career Change Interest'] = int(input("Career Change Interest (1 for Yes, 0 for No): "))

    return user_input


# User Input and Recommendation Generator

user_input = get_user_input()

hybrid_results = hybrid_recommender(
    user_input=user_input,
    df=career_df,
    scaled_df=scaled_df,
    scaler=scaler,
    kmeans_model=kmeans,
    tfidf_matrix=tfidf_matrix,
# Control the weight: 1 = content-based, 0 = collaborative-based
    alpha=0.43
)

print("\Recommended Occupations:", hybrid_results)
