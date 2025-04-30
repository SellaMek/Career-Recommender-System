# Career-Recommender-System
  - Start date: 01/2025
  - DSC 4900: Data Science Project / Portfolio @ Belmont University
  - Author: Sella Mekonnen


Table of Contents
---
   * [About the Project](#about-the-project)
   * [Source Data & Preprocessing](#source-data-preprocessing)
   * [Methodology](#methodology)
   * [Results](#results)
   * [ADVANCED TOPICS](#advanced-topics)


## About the Project
Traditional career guidance often relies on generalized advice, human counselors, or further strategies that offer limited personalization. In contrast, employing machine learning-based career recommender systems utilizes data to connect individuals with suitable career paths based on their interests, skills, and industry trends.

This project develops a Career Recommender System using the Field of Study vs. Occupation dataset from Kaggle to analyze key factors such as job satisfaction, industry growth rate, and work-life balance. By integrating methodologies such as natural language processing (NLP), K-Means clustering, and feature engineering, the system filters careers and users to deliver personalized recommendations. The objective of the Career Recommender System is to aid individuals in taking a step towards making more informed career decisions.

## Source Data & Preprocessing
## 📊 Dataset Overview

- **Primary Data Source:**  
  The core dataset used in this project is from **Kaggle: Field of Study vs Occupation**.  
  [View on Kaggle](https://www.kaggle.com/datasets/jahnavipaliwal/field-of-study-vs-occupation)

The source data for this study comes from Field Of Study vs Occupation 1. This is a public dataset through Kaggle which is designed to offer an opportunity for various exploratory studies, including machine learning models. The source data is rich in that it contains 22 attributes and over 30,000 records of factors that concern the occupation of individuals. Below is a snapshot of a few of these features along with the distribution of the occupations.

<img width="700" alt="source_data_screenshot" src="https://github.com/user-attachments/assets/bf407512-249e-41f6-93dd-31ee168ffab2" />

The dataset contains numerous useful features that are able to be leveraged to facilitate offering occupation recommendation for individuals based on their academic background, job preferences, and other factors. 
The resulting data was consolidated by means of pre-processing, cleaning, and feature engineering which. This enabled the building of a recommender system which can suggest a career based on a user’s information.



- **Additional Data (Planned):**  
  We plan to **web-scrape** career descriptions using the  
  **U.S. Bureau of Labor Statistics Occupational Outlook Handbook**:  
  [Occupational Outlook Handbook A-Z Index](https://www.bls.gov/ooh/a-z-index.htm)

---

### 📈 Data Volume

- **Rows:** 38,444  
- **Total Features:** 22  
- **Missing Data:**  
  - `Family Influence` feature has **9,632 missing entries** and will be **dropped** from the analysis.

---

### ⚠️ Limitations

- The dataset includes only **10 unique occupations**, which limits the variety in recommendations:

## 📊 Exploratory Data Analysis (EDA)

To better understand the structure and quality of the dataset, I performed a series of exploratory steps and visualizations.

---

### 🧮 Initial Dataset Overview

- The dataset was loaded and inspected using `.head()` to view the first few entries.
- A `.count()` check was conducted to confirm how many non-null values were present per column.

---

### ❗ Missing Data

I identified missing values in several columns using `.isnull().sum()`. The most notable case was:

- `Family Influence`: 9,632 missing entries  
  👉 This feature was **dropped** due to the large volume of missing data.

---

### 💼 Unique Categories

I explored the variety of occupations and fields of study:

- **Current Occupations:**  
  The dataset contains **10 unique occupations** including:  
  `['Business Analyst', 'Economist', 'Biologist', 'Doctor', 'Lawyer', 'Software Developer', 'Artist', 'Psychologist', 'Teacher', 'Mechanical Engineer']`

- **Fields of Study:**  
  The dataset includes a broader range of unique fields, such as Computer Science, Biology, Engineering, Law, Psychology, and more.

---

### 📊 Visualizations

#### Distribution of Current Occupations

![Occupation Distribution](#)

A `countplot` was used to display the distribution of the 10 current occupations in the dataset. This plot helped highlight which roles are most frequently represented.

#### Distribution of Fields of Study

![Field of Study Distribution](#)

Another `countplot` visualized the distribution of various fields of study among individuals in the dataset.

#### Distribution of Education Level

![Education Level Distribution](#)

This chart shows how different education levels are represented in the dataset, revealing patterns in academic backgrounds tied to career paths.

---

These insights were used to inform feature engineering, model design, and limitations in recommendation diversity.



## Methodology
he Career Recommender System is developed through a hybrid model of content-based filtering and collaborative filtering. The data processing began by consolidating the dataset to incorporate features that captured both the user’s background and job information. 

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
