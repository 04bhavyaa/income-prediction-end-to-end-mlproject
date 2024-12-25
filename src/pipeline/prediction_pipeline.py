# Create Prediction Pipeline Class
# Create function load object
# Create custom class based on our dataset
# Create function to convert our data into dataframe with dict

import os
import sys
# Add the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object
import numpy as np
import pandas as pd
from dataclasses import dataclass

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        preprocessor_path = os.path.join("artifacts/data_transformation", "preprocessor.pkl")
        model_path = os.path.join("artifacts/model_trainer", "model.pkl")

        processor = load_object(preprocessor_path)
        model = load_object(model_path)

        data_scaled = processor.transform(features)
        pred = model.predict(data_scaled)
        return pred
    
class CustomClass:
    def __init__ (self, 
                  age:int, 
                  workclass:int, 
                  education_num:int, 
                  marital_status:int, 
                  occupation:int, 
                  relationship:int, 
                  race:int, 
                  sex:int, 
                  capital_gain:int, 
                  capital_loss:int, 
                  hours_per_week:int
                  ):
        self.age = age
        self.workclass = workclass
        self.education_num = education_num
        self.marital_status = marital_status
        self.occupation = occupation
        self.relationship = relationship
        self.race = race
        self.sex = sex
        self.capital_gain = capital_gain
        self.capital_loss = capital_loss
        self.hours_per_week = hours_per_week

    def get_data_as_dataframe(self):
        try:
            custom_data_input = {
                "age": [self.age],
                "workclass": [self.workclass],
                "education_num": [self.education_num],
                "marital_status": [self.marital_status],
                "occupation": [self.occupation],
                "relationship": [self.relationship],
                "race": [self.race],
                "sex": [self.sex],
                "capital_gain": [self.capital_gain],
                "capital_loss": [self.capital_loss],
                "hours_per_week": [self.hours_per_week]
            }
            data = pd.DataFrame(custom_data_input)
            return data
        
        except Exception as e:
            raise CustomException(e, sys)
