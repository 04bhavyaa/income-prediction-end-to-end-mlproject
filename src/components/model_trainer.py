import os, sys
import pandas as pd
import numpy as np
# Add the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object, evaluate_model
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

class ModelTrainerConfig:
    train_model_file_path = os.path.join("artifacts/model_trainer", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Model trainer initiated")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1], 
                train_array[:, -1], 
                test_array[:, :-1], 
                test_array[:, -1]
            )

            models = {
                "Logistic Regression": LogisticRegression(),
                "Decision Tree": DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier()
            }

            params = {
                "Logistic Regression": {
                    'class_weight': ['balanced', None],
                    'penalty': ['l1', 'l2'],
                    'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                    'solver': ['liblinear', 'saga']
                },
                "Decision Tree": {
                    'class_weight': ['balanced', None],
                    'criterion': ['gini', 'entropy', 'log_loss'],
                    'splitter': ['best', 'random'],
                    'max_depth': [2, 3,4,5, 6, 8, 10],
                    'min_samples_split': [2, 3,4,5, 10],
                    'min_samples_leaf': [1, 2,3, 4],
                    'max_features': ['auto', 'sqrt', 'log2']
                },
                "Random Forest": {
                    'class_weight': ['balanced', None],
                    'n_estimators': [100, 200, 300, 400, 500],
                    'max_depth': [2, 3,4,5, 6, 8, 10],
                    'min_samples_split': [2, 3,4,5, 10],
                }
            }

            model_report:dict = evaluate_model(X_train = X_train, y_train = y_train, X_test = X_test, y_test =y_test,
                                                models = models, params = params)
            
            # To gest best model from our report Dict
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(models.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]
            
            print(f"Best Model Found, Model Name is: {best_model_name},Accuracy_Score: {best_model_score}")
            logging.info(f"best model found, Model Name is {best_model_name}, accuracy Score: {best_model_score}")

            save_object(file_path=self.model_trainer_config.train_model_file_path,
                        obj = best_model
                        )
        except Exception as e:
            raise CustomException(e, sys)