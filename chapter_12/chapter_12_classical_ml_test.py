# 
# This workbook shows how to test a classical machine learning model
# What it does is that it takes a model that has been previously saved
# and then it uses it to predict the class of a new instance
# which is an instance that has been prepared before
#

# import the libraries pandas and joblib
import pandas as pd
import joblib

# load the model
model = joblib.load('./chapter_12_decision_tree_model.joblib')

# load the data which we used for training before
dfDataAnt13 = pd.read_excel('./chapter_12.xlsx', 
                            sheet_name='ant_1_3',
                            index_col=0)


# test that the model is not null
# which means that it actually exists
def test_model_not_null():
    assert model is not None

# test that the model predicts class 1 correctly
# here correctly means that it predicts the same way as when it was trained
def test_model_predicts_class_correctly():
    X = dfDataAnt13.drop(['Defect'], axis=1)
    assert model.predict(X)[0] == 1

# test that the model predicts class 0 correctly
# here correctly means that it predicts the same way as when it was trained
def test_model_predicts_class_0_correctly():
    X = dfDataAnt13.drop(['Defect'], axis=1)
    assert model.predict(X)[1] == 0