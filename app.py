from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('new_model.pickle', 'rb'))
scaler = pickle.load(open('new_scaler.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        cgpa = float(request.form['cgpa'])
        iq = float(request.form['iq'])
        print("cgpa ---> ",cgpa)
        print("iq ---> ",iq)


        features = np.array(scaler.transform([[cgpa, iq]]))
        prediction = model.predict(features)[0]

        print('Prediction --->',prediction)
        
        result = 'Placed' if prediction == 1 else 'Not Placed'
        return jsonify({'result': result})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
