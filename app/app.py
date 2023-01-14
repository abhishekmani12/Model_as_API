from flask import Flask, jsonify, request
#import json
from sklearn.ensemble import GradientBoostingClassifier
import pickle as pkl
import pandas as pd

app = Flask(__name__)



def load_model():
    global model
    with open('gbmodel.pkl', 'rb') as f:
        model = pkl.load(f)
        
load_model()

@app.route('/')
def home_endpoint():
    return 'hello'


@app.route('/pred', methods=['GET','POST'])
def get_prediction():
    if (request.method == 'GET') or (request.method == 'POST'):
        jdata = request.get_json()
        qdf=pd.DataFrame(jdata)
        pred=model.predict(qdf)
        send="Survives" if pred == 1 else "Dies"
    else:
        send="Invalid"
    return jsonify(send)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
