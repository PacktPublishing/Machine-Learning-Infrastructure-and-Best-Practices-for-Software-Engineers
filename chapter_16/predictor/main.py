#
# This is a flask web service to make predictions on the data
# that is sent to it. It is meant to be used with the measurement instrument
# 
from flask import *  
from joblib import load
import pandas as pd 

app = Flask(__name__)   # create an app instance

# entry point where we send JSON with two parameters: 
# LOC and MCC
# and make prediction using make_prediction method
@app.route('/predict/<loc>/<mcc>')
def predict(loc,mcc):
    return {'Defect': make_prediction(loc, mcc)}

@app.route('/')
def hello():
    return 'Welcome to the predictor! You need to send a GET request with two parameters: LOC (lines of code) and MCC (McCabe complexity))'

# the main method for making the prediction
# using the model that is stored in the joblib file
def make_prediction(loc, mcc):
    # now read the model from the joblib file
    # and predict the defects for the X_test data
    
    dt = load('dt.joblib')

    # input data to the model
    input = {'LOC': loc, 
             'MCC': mcc}
    
    # convert input data into dataframe
    X_pred = pd.DataFrame(input, index=[0])

    # make prediction
    y_pred = dt.predict(X_pred)

    # return the prediction
    # as an integer
    return int(y_pred[0])    

# run the application
if __name__ == '__main__':   
    app.run(port=5001, debug=True)