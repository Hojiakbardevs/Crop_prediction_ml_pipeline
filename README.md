# Crop Yield Prediction using Machine Learning 

## Overview

This project aims to predict the quantity of production for various types of crops using Machine Learning. 
The project consists of four main components:

- Data Ingestion, 
- Data Transformation, 
- Model Training, 
- Prediction Pipeline.

## Project Structure

### components/:
Contains modules for data ingestion, data transformation, and model training.
###utils/: 
Contains utility functions for logging, exception handling, and saving/loading objects.
###src/: 
Contains the main application code and prediction pipeline.
###dataset/:
Folder to store dataset files and trained models.
###logs/: 
Folder to store logs generated during the project.

##Installation
To install the required packages, run:
pip install -r requirements.txt

## Data Ingestion
### Data Source
The data for this project is retrieved from a MongoDB database. The data consists of various features related to crop production, such as N, P, K nutrient levels, pH, rainfall, temperature, area in hectares, state name, crop type, and crop.
Process
Connect to MongoDB and retrieve data.
Save the data as a CSV file.
Split the data into training and testing sets.

## Data Transformation
### Preprocessing
The data undergoes the following preprocessing steps:

#### Imputation: 
Missing values are imputed using median for numerical features and most frequent value for categorical features.
### Scaling:
Numerical features are scaled using StandardScaler.
### Encoding:
Categorical features are encoded using OrdinalEncoder.



## Pipeline
The preprocessing steps are combined into a pipeline using ColumnTransformer.

## Model Training
Models Used
Several regression models are trained and evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet Regression
- Decision Tree Regression
- Random Forest Regression


## Evaluation
The models are evaluated using R-squared score on the test set. The best-performing model is saved for future predictions.



## Prediction Pipeline
The prediction pipeline consists of two main parts:

## Data Input:
User inputs the features required for prediction through a web form.
Prediction: The selected model predicts the crop yield based on the input features.


## Deployment
The project has been deployed on an AWS EC2 instance and is accessible via the following link:

http://ec2-52-70-34-66.compute-1.amazonaws.com:8050/predict

## Dataset
The dataset used in this project is taken from Kaggle and can be found here.










