import pickle

from flask import Flask
from flask import request
from flask import jsonify


with open('src/model_files/model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)

with open('src/model_files/dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        customer = request.get_json()

        X = dv.transform([customer])
        y_pred = model.predict_proba(X)[0, 1]
        churn = y_pred >= 0.5

        result = {
            'churn_probability': float(y_pred),
            'churn': bool(churn)
        }
    else:
        result = {"hello": "world"}

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
