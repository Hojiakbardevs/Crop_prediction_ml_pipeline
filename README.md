# Crop Yield Prediction using Machine Learning 

## Overview

This project aims to predict the quantity of production for various types of crops using Machine Learning. 
The project consists of four main components:

- Data Ingestion, 
- Data Transformation, 
- Model Training, 
- Prediction Pipeline.

## Project Structure

 **src/:**  Contains the main application code and prediction pipeline.
 **components/:** Contains modules for data ingestion, data transformation, and model training.
 pipeline
 **pipeline/:** Contains two main pipelines - prediction_pipeline and train_pipeline.
 **logs/:** Folder to store logs generated during the project.
 **utils/:** Contains utility functions for logging, exception handling,  saving/loading objects and extracting data from mongodb.
 **exception/:** To handle exceptions and raise custom exceptions with detailed error messages.


## Installation
To install the required packages, run:
pip install -r requirements.txt
- numpy==1.26.4
- pandas==2.2.2
- flask==3.0.3
- scikit-learn==1.4.2
- seaborn==0.13.2
- pymongo==4.6.3
- datetime==5.5


##Pipeline Overview
The project pipeline consists of the following stages:

**Data Ingestion:** Connect to MongoDB and retrieve the dataset.
**Data Preprocessing:** Handle missing values, scale numerical features, and encode categorical features.
**Model Training:** Train various regression models to predict crop yields.
**Model Evaluation:** Evaluate the trained models using R-squared score.
**Prediction:** Deploy the best-performing model for crop yield prediction via a web interface.


## Data Ingestion
**Data Source:** The dataset is retrieved from a MongoDB database. It includes features such as nutrient levels (N, P, K), pH, rainfall, temperature, area in hectares, state name, crop type, and crop.

**Process**
- Connect to MongoDB and retrieve data.
- Save the data as a CSV file.
- Split the data into training and testing sets.

## Data Transformation
**Preprocessing:** The data undergoes the following preprocessing steps:
**Imputation:**  Missing values are imputed using median for numerical features and most frequent value for categorical features.
**Scaling:** Numerical features are scaled using StandardScaler.
**Encoding:** Categorical features are encoded using OrdinalEncoder.



**Pipeline:** The preprocessing steps are combined into a pipeline using ColumnTransformer.

## Model Training
**Models Used**
Several regression models are trained and evaluated:
- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet Regression
- Decision Tree Regression
- Random Forest Regression



## Evaluation
The models are evaluated using R-squared score on the test set. The best-performing model is saved for future predictions.



##Prediction Pipeline

The **prediction_pipeline** folder contains the following components:

**PredictPipeline Class:** This class loads the preprocessed data and the trained model to make predictions.

**CustomData Class:** This class takes input features and converts them into a DataFrame suitable for prediction.


## Deployment
The project has been deployed on an AWS EC2 instance and is accessible via the following link:


**[http://ec2-52-70-34-66.compute-1.amazonaws.com:8050/predict](http://ec2-52-70-34-66.compute-1.amazonaws.com:8050/predict)**

## Usage
To run the prediction web application locally, execute:
**python app.py**
Visit **[http://localhost:5000](http://127.0.0.1:5000/)** in your web browser to use the application.

## Dataset
The dataset used in this project is taken from Kaggle and can be found here.

**[https://www.kaggle.com/datasets/gautamshah2002/india-crop-data-with-validation](https://www.kaggle.com/datasets/gautamshah2002/india-crop-data-with-validation)**









