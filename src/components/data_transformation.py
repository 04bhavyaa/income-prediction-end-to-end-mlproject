# Handle missing data
# Handle Imbalanced data
# Outlier Handling
# Convert Categorical to Numerical data

import os, sys
import pandas as pd
import numpy as np
# Add the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.logger import logging
from src.exception import CustomException
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils import save_object

class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts/data_transformation", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info("Data Transformation object created")
            numerical_features = ['age', 'workclass', 'education_num', 'marital_status', 'occupation', 'relationship', 
                                  'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week']
            
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')), # to handle missing data
                    ('scaler', StandardScaler()) # to bring all the features to the same scale
                ]
            )
            
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num_pipeline', num_pipeline, numerical_features)
                ]
            )
            
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        
    def remove_outliers_IQR(self, col, data):
        try:
            Q1 = data[col].quantile(0.25)
            Q3 = data[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            data.loc[(data[col]>upper_bound, col)] = upper_bound
            data.loc[(data[col]<lower_bound, col)] = lower_bound
            logging.info(f"Outliers removed in [{col}] using IQR")
            return data
        except Exception as e:
            logging.info("Error in removing outliers")
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Data transformation initiated")
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            numerical_features = ['age', 'workclass', 'education_num', 'marital_status', 'occupation', 'relationship', 
                                  'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week']
            
            for feature in numerical_features:
                self.remove_outliers_IQR(col=feature, data=train_data)
            logging.info("Outliers capped in train data")
            for feature in numerical_features:
                self.remove_outliers_IQR(col=feature, data=test_data)
            logging.info("Outliers capped in test data")

            preprocess_obj = self.get_data_transformation_object()
            target_column = 'income'
            drop_columns = [target_column]

            logging.info("Splitting data into Dependent and Independent Features")
            input_train_data = train_data.drop(columns=drop_columns, axis=1)
            target_train_data = train_data[target_column]
            input_test_data = test_data.drop(columns=drop_columns, axis=1)
            target_test_data = test_data[target_column]

            # Apply transformation on train and test data
            input_train_arr = preprocess_obj.fit_transform(input_train_data)
            input_test_arr = preprocess_obj.transform(input_test_data)

            # Apply preprocessor object on test and train data
            train_array = np.c_[input_train_arr, np.array(target_train_data)]
            test_array = np.c_[input_test_arr, np.array(target_test_data)]

            # Save preprocessor object
            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path, 
                        obj=preprocess_obj)
            logging.info("Preprocessor object saved")
            logging.info("Data transformation is successful")
            return (train_array, test_array, self.data_transformation_config.preprocessor_obj_file_path)

        except Exception as e:
            logging.info("Error in data transformation")
            raise CustomException(e, sys)
            