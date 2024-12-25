import sys,os
from flask import Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.logger import logging
from src.exception import CustomException

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        raise Exception ("This is a test exception")
    except Exception as e:
        abc = CustomException(e, sys)
        logging.info(abc.error_message)
        return ("Income Prediction")

if __name__ == "__main__":
    app.run(debug=True)