# 
# This file contains the gradio application, which is a user interface to our ML model
# It is probably the easiest way to deploy a model as it requires minimal overhead
#

import gradio as gr
import pandas as pd
from diffusers import StableDiffusionPipeline
import torch

def generate_images(prompt):
    '''
    This function uses the prompt to generate an image
    using the anything 4.0 model from Hugging Face
    '''
    
    # importing the model from Hugging Face
    model_id = "xyn-ai/anything-v4.0"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, 
                                                   torch_dtype=torch.float16, 
                                                   safety_checker=None)

    # send the pipeline to the GPU for faster processing
    pipe = pipe.to("cuda")

    # create the image here
    image = pipe(prompt).images[0]
    
    # return the number of defects
    return image

# This is where we integrate the function above with the user interface
# for this, we need to create an input box for each of the following parameters:
# CBO, DCC, ExportCoupling,	ImportCoupling,	NOM,	WMC

demo = gr.Interface(fn=generate_images,                                         
                    inputs = 'text',
                    outputs = 'image')

# and here we start the actual user interface
# in a browser window
demo.launch()