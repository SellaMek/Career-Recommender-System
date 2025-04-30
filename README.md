# Career-Recommender-System
  - Start date: 01/2025
  - DSC 4900: Data Science Project / Portfolio @ Belmont University
  - Author: Sella Mekonnen


Table of Contents
---
   * [About the Project](#about-the-project)
   * [Source Data](#source-data)
   * [Preprocessing](#preprocessing)
   * [Methodology](#methodology)
   * [Results](#results)
   * [Advanced Topics](#advanced-topics)


## About the Project
Traditional career guidance often relies on generalized advice, human counselors, or further strategies that offer limited personalization. In contrast, employing machine learning-based career recommender systems utilizes data to connect individuals with suitable career paths based on their interests, skills, and industry trends.

This project develops a Career Recommender System using the Field of Study vs. Occupation dataset from Kaggle to analyze key factors such as job satisfaction, industry growth rate, and work-life balance. By integrating methodologies such as natural language processing (NLP), K-Means clustering, and feature engineering, the system filters careers and users to deliver personalized recommendations. The objective of the Career Recommender System is to aid individuals in taking a step towards making more informed career decisions.

## Source Data
Source Data
The source data for this study comes from Field Of Study vs Occupation 1. This is a public dataset through Kaggle which is designed to offer an opportunity for various exploratory studies, including machine learning models. The source data is rich in that it contains 22 attributes and over 30,000 records of factors that concern the occupation of individuals. Below is a snapshot of a few of these features along with the distribution of the occupations.

<img width="700" alt="source_data_screenshot" src="https://github.com/user-attachments/assets/bf407512-249e-41f6-93dd-31ee168ffab2" />

The dataset contains numerous useful features that are able to be leveraged to facilitate offering occupation recommendation for individuals based on their academic background, job preferences, and other factors. 
The resulting data was consolidated by means of pre-processing, cleaning, and feature engineering which. This enabled the building of a recommender system which can suggest a career based on a user’s information.

## Results
The Career Recommender System results in a user interaction which prompts the user to input their information. The Command Line Interface (CLI) based form allows the individual to insert background and career-interest information. The user inputs are a combination of numerical and binary values, as shown in Figure 3. 
To test the accuracy of the recommender system, a random user input generator which is then compared to the random user’s actual top nearest occupations was implemented. An accuracy score was then calculated based on the two factors. This resulted in an accuracy score of 0.6667 on average. While this score is not high, it does indicate that, on average, the recommender system suggests the user with 2 out of 3 careers that align with their actual nearest occupations.

<img width="566" alt="results_screenshot" src="https://github.com/user-attachments/assets/a3a284a9-7175-44eb-9e70-7908fcfc6046" />


## Further Steps
The Career Recommender System is currently at a functional stage which can provide career suggestions to users based on the information they enter concerning their background and job interest. While the current version of the system is able to provide recommendations based on the limited information that it contains about each occupation title, refinements can be contribute to the enhancement of the system’s accuracy. One of the goals to step towards an elevated dataset is by appending descriptions of each occupation title. This can be done through web scraping in order to retrieve supplemental data for the system to improve its accuracy through NLP. This step is currently in the works for future implementation.

An additional objective is to create a user interface which allows individuals to utilize the Career Recommender System along with implementation of more specific questions targeting a wider range of career options. Along with this can be the integration of connecting users to sources that provide current available jobs within the field that they are suggested and would like to explore.

