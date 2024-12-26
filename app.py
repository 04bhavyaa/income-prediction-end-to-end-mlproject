import streamlit as st
import pandas as pd
from src.pipeline.prediction_pipeline import PredictionPipeline, CustomClass

# Title of the app
st.title("Yearly Income Prediction")
st.write("Predict whether your yearly income is more or less than $50k based on various factors.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, value=25, step=1)

# Mapping dictionary for workclass
workclass_mapping = {
    "State-gov": 6,
    "Self-emp-not-inc": 5,
    "Private": 3,
    "Federal-gov": 0,
    "Local-gov": 1,
    "Self-emp-inc": 4,
    "Without-pay": 7,
    "Never-worked": 2
}

# Get the string value from selectbox
workclass = st.selectbox(
    "Workclass",
    options=list(workclass_mapping.keys()),  # Use the keys from the mapping
    format_func=lambda x: x  # Display the string (same as the key)
)
workclass_int = workclass_mapping[workclass]  # Get the value from the mapping

education_mapping = {
        "10th": 0,
        "11th": 1,
        "12th": 2,
        "1st-4th": 3,
        "5th-6th": 4,
        "7th-8th": 5,
        "9th": 6,
        "Assoc-voc": 7,
        "Bachelors": 8,
        "Doctorate": 9,
        "HS-grad": 10,
        "Masters": 11,
        "Preschool": 12,
        "Prof-school": 13,
        "Some-college": 14
    }
# Get the string value from selectbox
education = st.selectbox(
    "Education Level",
    options=list(education_mapping.keys()),  # Use the keys from the mapping
    format_func=lambda x: x  # Display the string (same as the key)
)
education_int = education_mapping[education]  # Get the value from the mapping

marital_status_mapping = {
        "Never-married": 4,
        "Married-civ-spouse": 2,
        "Divorced": 0,
        "Married-spouse-absent": 3,
        "Separated": 5,
        "Married-AF-spouse": 1,
        "Widowed": 6
    }

# Get the string value from selectbox
marital_status = st.selectbox(
    "Marital Status",
    options=list(marital_status_mapping.keys()),  # Use the keys from the mapping
    format_func=lambda x: x  # Display the string (same as the key)
)
marital_status_int = marital_status_mapping[marital_status]  # Get the value from the mapping

occupation_mapping = {
        "Adm-clerical": 0,
        "Exec-managerial": 3,
        "Handlers-cleaners": 5,
        "Prof-specialty": 9,
        "Other-service": 7,
        "Sales": 11,
        "Craft-repair": 2,
        "Transport-moving": 13,
        "Farming-fishing": 4,
        "Machine-op-inspct": 6,
        "Tech-support": 12,
        "Protective-serv": 10,
        "Armed-Forces": 1,
        "Priv-house-serv": 8
    }

# Get the string value from selectbox
occupation = st.selectbox(
    "Occupation",
    options=list(occupation_mapping.keys()),  # Use the keys from the mapping
    format_func=lambda x: x  # Display the string (same as the key)
)
occupation_int = occupation_mapping[occupation]  # Get the value from the mapping

relationship_mapping ={
        "Not-in-family": 1,
        "Husband": 0,
        "Wife": 5,
        "Own-child": 3,
        "Unmarried": 4,
        "Other-relative": 2
    }

# Get the string value from selectbox
relationship = st.selectbox(
    "Relationship",
    options=list(relationship_mapping.keys()),  # Use the keys from the mapping
    format_func=lambda x: x  # Display the string (same as the key)
)
relationship_int = relationship_mapping[relationship]  # Get the value from the mapping

race_mapping = {
        "White": 4,
        "Black": 2,
        "Asian-Pac-Islander": 1,
        "Amer-Indian-Eskimo": 0,
        "Other": 3
    }

# Get the string value from selectbox
race = st.selectbox(
    "Race",
    options=list(race_mapping.keys()),  # Use the keys from the mapping
    format_func=lambda x: x  # Display the string (same as the key)
)
race_int = race_mapping[race]  # Get the value from the mapping

sex_mapping = {
        "Female": 0,
        "Male": 1
    }

# Get the string value from selectbox
sex = st.selectbox(
    "Sex",
    options=list(sex_mapping.keys()),  # Use the keys from the mapping
    format_func=lambda x: x  # Display the string (same as the key)
)
sex_int = sex_mapping[sex]  # Get the value from the mapping

native_country_mapping = {
        "United-States": 38,
        "Cuba": 4,
        "Jamaica": 22,
        "India": 18,
        "Mexico": 25,
        "South": 34,
        "Puerto-Rico": 32,
        "Honduras": 15,
        "England": 8,
        "Canada": 1,
        "Germany": 10,
        "Iran": 19,
        "Philippines": 29,
        "Italy": 21,
        "Poland": 30,
        "Columbia": 3,
        "Cambodia": 0,
        "Thailand": 36,
        "Ecuador": 6,
        "Laos": 24,
        "Taiwan": 35,
        "Haiti": 13,
        "Portugal": 31,
        "Dominican-Republic": 5,
        "El-Salvador": 7,
        "France": 9,
        "Guatemala": 12,
        "China": 2,
        "Japan": 23,
        "Yugoslavia": 40,
        "Peru": 28,
        "Outlying-US(Guam-USVI-etc)": 27,
        "Scotland": 33,
        "Trinadad-Tobago": 37,
        "Greece": 11,
        "Nicaragua": 26,
        "Vietnam": 39,
        "Hong": 16,
        "Ireland": 20,
        "Hungary": 17,
        "Holand-Netherlands": 14
    }

# Get the string value from selectbox
native_country = st.selectbox(
    "Native Country",
    options=list(native_country_mapping.keys()),  # Use the keys from the mapping
    format_func=lambda x: x  # Display the string (same as the key)
)
native_country_int = native_country_mapping[native_country]  # Get the value from the mapping

capital_gain = st.number_input("Capital Gain", min_value=0, value=0, step=1)
capital_loss = st.number_input("Capital Loss", min_value=0, value=0, step=1)
hours_per_week = st.number_input("Hours Per Week", min_value=1, max_value=168, value=40, step=1)

# When the "Predict" button is clicked
if st.button("Predict"):
    # Create an instance of CustomClass with user inputs
    data = CustomClass(
        age=int(age),
        workclass=int(workclass_int),
        education=int(education_int),
        marital_status=int(marital_status_int),
        occupation=int(occupation_int),
        relationship=int(relationship_int),
        race=int(race_int),
        sex=int(sex_int),
        capital_gain=int(capital_gain),
        capital_loss=int(capital_loss),
        hours_per_week=int(hours_per_week),
        native_country=int(native_country_int)
    )

    # Convert input data into a DataFrame
    final_data = data.get_data_as_dataframe()

    # Make prediction
    pipeline_prediction = PredictionPipeline()
    pred = pipeline_prediction.predict(final_data)

    # Display the result
    if pred[0] == 0:
        st.success("Your Yearly Income is Less than or Equal to $50k.")
    else:
        st.success("Your Yearly Income is More than $50k.")