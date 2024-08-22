# Placement Predictor

Welcome to the **Placement Predictor**! This web application predicts whether a student will be placed or not based on their CGPA and IQ.

## Project Overview

The Placement Predictor uses Logistic Regression machine learning algorithm to assess a student's likelihood of getting placed based on two key metrics:

- **CGPA**: The student's cumulative grade point average.
- **IQ**: The student's intelligence quotient.

By inputting these values into the predictor, users can receive a prediction of either "Placed" or "Not Placed."

## Live Demo

You can try the Placement Predictor by visiting the following link:

[Placement Predictor - Live Demo](https://placement-predictor-4.onrender.com/)
It may take some time to launch ( not more than 50 sec, please wait )

## Features

- **User-friendly Interface**: The application has a clean and simple interface, making it easy for users to input their data and get predictions.
- **Real-time Predictions**: The application provides instant predictions as soon as the user submits their CGPA and IQ values.
- **Machine Learning Model**: The predictor is powered by a trained machine learning model that has been fine-tuned for accuracy.

## Project Structure

- **`app.py`**: The main Flask application file that routes requests and serves the web pages.
- **`index.html`**: The main HTML file located in the `templates` directory that provides the user interface.
- **`new_model.pickle`**: The serialized machine learning model used to make predictions.
- **`new_scaler.pickle`**: The serialized scaler used for preprocessing the input data.
- **`static/`**: Directory containing static files such as images, media etc.(This folder is important for flask application to know about static files)
- **`templates/`**: Directory containing HTML templates for the application.

## Getting Started

To run this project locally, follow these steps:

1. **Clone the Repository:**

```
  git clone https://github.com/yourusername/placement-predictor.git
  cd placement-predictor
  ```


2. Create and activate a virtual environment** (optional but recommended):

 ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 ```


3. Install the Required Python Packages

 ```
pip install -r requirements.txt
 ```


4. Run the Application

Start the Flask application:

```
python app.py

```


The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### How to Use

1. Open the application in your browser.
2. Enter your CGPA and IQ in the provided fields.
3. Click on the "Predict" button.
4. View your prediction on the screen.

