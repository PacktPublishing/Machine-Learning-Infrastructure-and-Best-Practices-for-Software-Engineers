import gradio as gr
from transformers import pipeline

pipe = pipeline("text-classification")

gr.Interface.from_pipeline(pipe).launch()