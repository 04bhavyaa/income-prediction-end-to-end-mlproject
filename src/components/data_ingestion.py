import os
import sys
# Add the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts/data_ingestion", "train.csv")
    test_data_path = os.path.join("artifacts/data_ingestion", "test.csv")
    raw_data_path = os.path.join("artifacts/data_ingestion", "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion initiated")
        try:
            logging.info("Reading data from source")
            data = pd.read_csv(os.path.join("notebook/data", "adult-income.csv"))
            logging.info("Data loaded successfully")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Data saved successfully")

            train_set, test_set = train_test_split(data, test_size=0.3, random_state=42)
            logging.info("Data split into train and test sets, successfully")
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Data ingestion is successful")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info(f"Error in data ingestion: {e}")
            raise CustomException(e,sys)
        

# src/components/data_ingestion.py