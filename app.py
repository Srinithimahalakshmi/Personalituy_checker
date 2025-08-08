from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('elasticnet_model.joblib')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    feature_names = model.named_steps['scaler'].get_feature_names_out()

    if request.method == 'POST':
        try:
            input_vals = [float(request.form[feature]) for feature in feature_names]
            arr = np.array([input_vals])
            pred = model.predict(arr)[0]
            prediction = f"{pred:.2f}"
        except:
            prediction = "Invalid input!"

    return render_template('index.html', prediction=prediction, features=feature_names)

if __name__ == '__main__':
    app.run(debug=True)
