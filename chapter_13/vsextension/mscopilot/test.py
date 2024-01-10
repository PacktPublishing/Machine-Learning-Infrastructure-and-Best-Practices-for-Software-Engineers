# read the line from stdin
# which is the text that we want to send to the model
prompt = input()

# executing the model and getting the data back
# TODO: write the code that will use the parrot model from HuggingFace 
# to generate suggestions of the code
from transformers import AutoTokenizer, AutoModelWithLMHead
  
tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot-small")
model = AutoModelWithLMHead.from_pretrained("codeparrot/codeparrot-small")

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model(**inputs)

# and then output from the model
print(f"\n ---- {prompt}: Hello world!, Finally, I arrived at the destination.")