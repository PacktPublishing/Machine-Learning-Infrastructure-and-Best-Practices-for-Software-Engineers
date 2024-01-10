# 
# This file contains the gradio application, which is a user interface to our ML model
# It is probably the easiest way to deploy a model as it requires minimal overhead
#

import gradio as gr
import pandas as pd
import joblib

def predict_defects(cbo, 
                    dcc, 
                    exportCoupling, 
                    importCoupling, 
                    nom, 
                    wmc):
    '''
    This function is called from the user interface. 

    It takes the following parameters:
    - cbo: Coupling between objects
    - dcc: Data complexity
    - exportCoupling: Export coupling
    - importCoupling: Import coupling
    - nom: Number of methods
    - wmc: Weighted methods per class

    It returns the following:
    - defects: The number of defects

    It uses the previously trained model (see chapter 12)
    '''
    # we need to convert the input parameters to floats
    cbo = float(cbo)
    dcc = float(dcc)
    exportCoupling = float(exportCoupling)
    importCoupling = float(importCoupling)
    nom = float(nom)
    wmc = float(wmc)

    # now, we need to make a data frame out of the input parameters
    # this is necessary because the model expects a data frame
    # with the following columns:
    # - cbo
    # - dcc
    # - exportCoupling
    # - importCoupling
    # - nom
    # - wmc

    # we create a dictionary with the column names as keys
    # and the input parameters as values
    # please note that the names of the features must be the same as in the model
    data = {
        'CBO': [cbo],
        'DCC': [dcc],
        'ExportCoupling': [exportCoupling],
        'ImportCoupling': [importCoupling],
        'NOM': [nom],
        'WMC': [wmc]
    }

    # we create a data frame from the dictionary  
    df = pd.DataFrame(data)

    # load the model
    model = joblib.load('./chapter_12_decision_tree_model.joblib')

    # predict the number of defects
    result = model.predict(df)[0]

    # return the number of defects
    return result

# This is where we integrate the function above with the user interface
# for this, we need to create an input box for each of the following parameters:
# CBO, DCC, ExportCoupling,	ImportCoupling,	NOM,	WMC

demo = gr.Interface(fn=predict_defects,                                         
                    inputs = ['number', 'number', 'number', 'number', 'number', 'number'],
                    outputs = gr.Textbox(label='Will contain defects?', 
                                         value= 'N/A'))

# and here we start the actual user interface
# in a browser window
demo.launch(share=True)