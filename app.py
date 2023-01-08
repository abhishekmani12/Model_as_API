from flask import Flask, jsonify, request
#import json
from sklearn.ensemble import GradientBoostingClassifier
import pickle as pkl
import pandas as pd

model = None
app = Flask(__name__)


def load_model():
    global model
    with open('gbmodel.pkl', 'rb') as f:
        model = pkl.load(f)


@app.route('/')
def home_endpoint():
    return 'hello'


@app.route('/pred', methods=['POST'])
def get_prediction():
    if request.method == 'POST':
        jdata = request.get_json()
        qdf=pd.DataFrame(jdata)
        pred=model.predict(qdf)
    return "Survives" if pred == 1 else "Dies :)"


if __name__ == '__main__':
    load_model()
    app.run(port=5000, debug=True)