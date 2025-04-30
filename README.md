# Career-Recommender-System
  - Start date: 01/2025
  - DSC 4900: Data Science Project / Portfolio @ Belmont University
  - Author: Sella Mekonnen


Table of Contents
---
   * [About the Project](#about-the-project)
   * [Source Data & Preprocessing](#source-data-preprocessing)
   * [Code Explained](#code-explained)
   * [Methodology](#methodology)
   * [Results](#results)
   * [ADVANCED TOPICS](#advanced-topics)


## About the Project
Traditional career guidance often relies on generalized advice, human counselors, or further strategies that offer limited personalization. In contrast, employing machine learning-based career recommender systems utilizes data to connect individuals with suitable career paths based on their interests, skills, and industry trends.

This project develops a Career Recommender System using the Field of Study vs. Occupation dataset from Kaggle to analyze key factors such as job satisfaction, industry growth rate, and work-life balance. By integrating methodologies such as natural language processing (NLP), K-Means clustering, and feature engineering, the system filters careers and users to deliver personalized recommendations. The objective of the Career Recommender System is to aid individuals in taking a step towards making more informed career decisions.

## Source Data & Preprocessing
## 📈 Dataset Overview

- **Primary Data Source:**  
  The core dataset used in this project is from **Kaggle: Field of Study vs Occupation**.  
  [View on Kaggle](https://www.kaggle.com/datasets/jahnavipaliwal/field-of-study-vs-occupation)

The source data for this study comes from Field Of Study vs Occupation 1. This is a public dataset through Kaggle which is designed to offer an opportunity for various exploratory studies, including machine learning models. The source data is rich in that it contains 22 attributes and over 30,000 records of factors that concern the occupation of individuals. Below is a snapshot of a few of these features along with the distribution of the occupations.

<img width="700" alt="source_data_screenshot" src="https://github.com/user-attachments/assets/bf407512-249e-41f6-93dd-31ee168ffab2" />

The dataset contains numerous useful features that are able to be leveraged to facilitate offering occupation recommendation for individuals based on their academic background, job preferences, and other factors. 
The resulting data was consolidated by means of pre-processing, cleaning, and feature engineering which. This enabled the building of a recommender system which can suggest a career based on a user’s information.

---

## 📊 Exploratory Data Analysis (EDA)

To better understand the structure and quality of the dataset, I performed a series of exploratory steps and visualizations.
---
### 📈 Data Volume

- **Rows:** 38,444  
- **Total Features:** 22  
- **Missing Data:**  
  - `Family Influence` feature has **9,632 missing entries** but was not used in the system, so it did not make an impact.

---

### ⚠️ Limitations

- The dataset includes only **10 unique occupations**, which limits the variety in recommendations.

---

### 💼 Unique Categories

I explored the variety of occupations and fields of study:

- **Current Occupations:**  
  The dataset contains **10 unique occupations** including:  
  `['Business Analyst', 'Economist', 'Biologist', 'Doctor', 'Lawyer', 'Software Developer', 'Artist', 'Psychologist', 'Teacher', 'Mechanical Engineer']`

- **Fields of Study:**  
  The dataset includes **10 unique fields**, such as Computer Science, Biology, Engineering, Law, Psychology, and more.

---



## Code Explained

### This explains the code used in building the hybrid Career Recommender System, which combines both content-based and collaborative filtering techniques.

---

**Encode Education Level**  
Education levels are converted from text categories (e.g., High School, Bachelor's, etc.) into numerical values, which are easier to process in machine learning models. The original column is replaced with this encoded version.

---

**Feature Selection**  
Two types of features are selected: numerical features like age and salary, and binary features like whether the user has certifications or freelancing experience. These features are used as inputs for model training.

---

**Data Scaling**  
All feature values are standardized to ensure that each feature contributes equally to the model. This helps improve the performance of clustering and similarity comparisons.

---

**KMeans Clustering**  
KMeans is used for collaborative filtering. It groups similar users into clusters based on their scaled feature profiles. Recommendations are based on the occupations of others within the same cluster.

---

**TF-IDF Vectorization**  
Text data in the "Current Occupation" column is vectorized using TF-IDF, which helps transform job titles into a numerical format that reflects the importance of each term. This enables content-based filtering.

---

**Hybrid Recommender Function**  
A custom function combines collaborative and content-based scores to produce personalized job recommendations. The content-based part identifies similar users based on overall profiles, while the collaborative part identifies users in the same KMeans cluster. Scores are weighted using an `alpha` parameter, and the highest-ranking jobs are recommended.

---

**Get User Input Function**  
A command-line interface prompts users to enter details about their age, experience, job preferences, and background. This input is processed and passed into the recommender system.

---

**Run the Recommender**  
After collecting user input, the recommender system generates personalized career recommendations based on a hybrid approach. The results are printed to the console.

---
### Random User

**Random User Input Generation**  
The function `generate_random_user_input()` generates a simulated user profile by randomly selecting values for various career-related features. This simulates the input that would be provided by a real user in the recommender system.

---

**Random Actual Occupations (Ground Truth)**  
The function `generate_random_actual_occupations()` selects 3 random occupations from the list of unique occupations in the dataset (`career_df['Current Occupation'].unique()`). These are used as the "actual" occupations for the randomly generated user input, representing the user's real career choices. This helps evaluate the accuracy of the recommender system by comparing the recommended occupations with the actual ones.

---

**Top-N Accuracy Calculation**  
The `calculate_top_n_accuracy()` function computes the accuracy of the recommender system by comparing the top-N recommended occupations with the actual (ground truth) occupations. It works as follows:
- **Predictions**: The list of recommended occupations.
- **Actual**: The actual occupations the user holds.
- **Top-N Accuracy**: The ratio of matching occupations from the top-N recommended occupations to the total number of top-N occupations (in this case, N=3). It checks if the recommended occupations appear in the actual occupations set.

This accuracy score gives an indication of how well the recommender system performs in suggesting the correct occupations.

---

**Hybrid Recommender System**  
The `hybrid_recommender()` function is used to get the top-N recommended occupations for a given user input. It combines both content-based filtering and collaborative filtering:
- **Content-Based Filtering**: Uses cosine similarity to compare the user’s features with other users' features to find the most similar profiles and recommend their occupations.
- **Collaborative Filtering**: Uses KMeans clustering to group similar users together. The recommender suggests occupations based on the cluster the user belongs to.

The function then returns the top-N recommended occupations, weighted by a given alpha parameter that controls the balance between the two methods.

---

**Evaluate Accuracy for Multiple Random Users**  
This block of code tests the accuracy of the recommender system across 10 randomly generated users:
1. **Generate random user input**: A random user profile is created using the `generate_random_user_input()` function.
2. **Select random actual occupation**: A random occupation is selected from the dataset to simulate the user’s actual job.
3. **Get hybrid recommendations**: The `hybrid_recommender()` function generates top-N career recommendations for the random user.
4. **Calculate accuracy**: The `evaluate_accuracy()` function calculates how many of the recommended occupations match the user’s actual occupation.
5. **Print results**: The results, including the actual occupation, recommended occupations, and top-N accuracy, are printed for each of the 10 random users.
6. **Accumulate accuracy**: The accuracy for each random user is added to a list, and the average top-N accuracy is calculated and printed at the end.

---

**Average Top-N Accuracy**  
At the end of the evaluation process, the average top-N accuracy across the 10 random users is calculated and displayed. This metric gives an overall indication of how well the recommender system is performing in terms of suggesting occupations that align with the actual career choices of the simulated users.

---
## Methodology
The Career Recommender System is developed through a hybrid model of content-based filtering and collaborative filtering. The data processing began by consolidating the dataset to incorporate features that captured both the user’s background and job information. 

Feature engineering was performed to encode categorical attributes (e.g., Education Level) from categorical to ordinal values. The dataset was also split into two feature types – numerical features and binary features – through feature selection. All the features were then standardized to normalize their scaling.

K-Means clustering was implemented for collaborative filtering. Each of the users were assigned to a cluster, as shown in Figure 1,  based on their profile. The system then retrieves the occupations of other users who are, in essence, similar peers in the same cluster.

<img width="504" alt="kmeans_screenshot" src="https://github.com/user-attachments/assets/a9dbfc99-ef2d-45ae-8919-63ec2f82913e" />

Natural Language Processing (NLP) was conducted for content-based filtering (Figure 2). This was done through a TF-IDF Vectorizer. This vectorizer was applied to the “Current Occupation” column in analyze the text data of each occupation. Cosine similarity was used to compare the user’s information to other users and find the 20 most similar individuals. The jobs of the similar users are then counted and normalized to generate scores.  

<img width="573" alt="tf_idf_screenshot" src="https://github.com/user-attachments/assets/f654ff81-599d-41d1-8037-c16e7659808a" />

A hybrid model was then developed by combining both the scores from collaborative and content-based filtering. The two scores are combined using a weighted average with an alpha value. The weight of alpha is a hyperparameter which can control the influence of each the scores. The alpha can be tuned to test which value will give the best accuracy. The system will finally return the top three highest-scoring occupations as recommendations to the user.


## Results
The Career Recommender System results in a user interaction which prompts the user to input their information. The Command Line Interface (CLI) based form allows the individual to insert background and career-interest information. The user inputs are a combination of numerical and binary values, as shown in Figure 3. 
To test the accuracy of the recommender system, a random user input generator which is then compared to the random user’s actual top nearest occupations was implemented. An accuracy score was then calculated based on the two factors. This resulted in an accuracy score of 0.6667 on average. While this score is not high, it does indicate that, on average, the recommender system suggests the user with 2 out of 3 careers that align with their actual nearest occupations.

<img width="566" alt="results_screenshot" src="https://github.com/user-attachments/assets/a3a284a9-7175-44eb-9e70-7908fcfc6046" />


## Further Steps
The Career Recommender System is currently at a functional stage which can provide career suggestions to users based on the information they enter concerning their background and job interest. While the current version of the system is able to provide recommendations based on the limited information that it contains about each occupation title, refinements can be contribute to the enhancement of the system’s accuracy. One of the goals to step towards an elevated dataset is by appending descriptions of each occupation title. This can be done through web scraping in order to retrieve supplemental data for the system to improve its accuracy through NLP. This step is currently in the works for future implementation.

An additional objective is to create a user interface which allows individuals to utilize the Career Recommender System along with implementation of more specific questions targeting a wider range of career options. Along with this can be the integration of connecting users to sources that provide current available jobs within the field that they are suggested and would like to explore.

- **Additional Data (Planned):**  
  I plan to **web-scrape** career descriptions using the  
  **U.S. Bureau of Labor Statistics Occupational Outlook Handbook**:  
  [Occupational Outlook Handbook A-Z Index](https://www.bls.gov/ooh/a-z-index.htm)

## ADVANCED TOPICS

### **📌 NLP (2 points)**
Natural Language Processing (NLP) was implemented using **TF-IDF Vectorization** on the `Current Occupation` field. This technique transformed occupation titles into numerical feature vectors by calculating the importance of each term across all job titles, while excluding common English stop words. These vectors were then used to compute **cosine similarity** between user profiles and existing occupations. This forms the **content-based filtering** component of the hybrid recommender system, helping to match users to careers that are textually similar to those held by others with similar backgrounds.

---

### **📌 K-Means Clustering (1 point)**
K-Means clustering was applied for collaborative filtering by segmenting users into distinct clusters based on shared characteristics. Before clustering, all selected numerical and binary features were standardized using `StandardScaler`. The algorithm grouped users into 5 clusters. When a new user input is provided, the system predicts the cluster they belong to and recommends careers commonly found in that group by learning from patterns among peer users.

---

### **📌 Feature Engineering (0.5 point)**
Feature engineering steps included:
- **Ordinal Encoding** of categorical data like education level (`High School` → 0, `Bachelor's` → 1, etc.).
- **Feature Selection** to isolate relevant `numerical_features` and `binary_features` for clustering and recommendation (e.g., Age, Job Satisfaction, Certifications, etc.).
- **Feature Scaling** using `StandardScaler` to normalize data and ensure equal weighting across features.

These transformations ensured the dataset was in optimal condition for both clustering and content-based similarity computations.

### **📌 Interactive Visualization (0.5 point)**
**Interactive Scatter Plot: Salary vs. Job Satisfaction**

This interactive scatter plot visualizes the relationship between salary and job satisfaction, with each point representing an individual from the dataset. 

- **X-axis:** Salary  
- **Y-axis:** Job Satisfaction  
- **Color:** K-Means cluster label  
- **Hover Info:** Current Occupation, Age, Years of Experience

<img width="1374" alt="interactive_vis_screenshot" src="https://github.com/user-attachments/assets/01441c79-da87-4ef9-b98d-f4b9948d27c5" />

### **📌 Web Scraping with Selenium (1 point)**
While the Web Scraping was not implemented into the final system, I did begin attempting it and found that it works for this. I simply wanted to add it here since I also included the code file to my repo, not in expectation of the point.

