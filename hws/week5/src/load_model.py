   
#!/usr/bin/env python
# coding: utf-8

import pickle

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

with open('src/model_files/model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)

with open('src/model_files/dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]
churn = y_pred >= 0.5

result = {
    'churn_probability': float(y_pred),
    'churn': bool(churn)
}

print(result)



