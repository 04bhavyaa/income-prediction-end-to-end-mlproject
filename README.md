## Income Prediction

The goal of this project is to predict whether an individual's income is greater than $50,000 or less than $50,000 based on various features. The dataset is derived from the UCI Adult Income dataset, which includes demographic and employment information of individuals. The task is to accurately classify individuals into one of two income categories: greater than $50K or less than or equal to $50K.

### Folder Structure
Directory structure:
└── 04bhavyaa-income-prediction-end-to-end-mlproject/
    ├── artifacts/
    │   ├── data_ingestion/
    │   │   ├── test.csv
    │   │   ├── raw.csv
    │   │   └── train.csv
    │   ├── model_trainer/
    │   │   └── model.pkl
    │   └── data_transformation/
    │       └── preprocessor.pkl
    ├── app.py
    ├── requirements.txt
    ├── setup.py
    ├── README.md
    ├── notebook/
    │   ├── income-prediction.ipynb
    │   └── data/
    │       ├── adult-income.csv
    │       └── adult.csv
    └── src/
        ├── logger.py
        ├── exception.py
        ├── components/
        │   ├── data_transformation.py
        │   ├── data_ingestion.py
        │   ├── __pycache__/
        │   └── model_trainer.py
        ├── __init__.py
        ├── __pycache__/
        ├── pipeline/
        │   ├── training_pipeline.py
        │   ├── __pycache__/
        │   └── prediction_pipeline.py
        └── utils.py

