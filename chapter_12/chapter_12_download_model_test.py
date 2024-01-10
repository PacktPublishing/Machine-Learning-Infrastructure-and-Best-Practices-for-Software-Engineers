#
# This is a test case for checking that a model has been downloaded correctly
# The model is the same as we used in the previous chapter
#

# import json to be able to read the embedding vector for the test
import json

# import the model via the huggingface library
from transformers import AutoTokenizer, AutoModelForMaskedLM

# load the tokenizer and the model for the pretrained SingBERTa
tokenizer = AutoTokenizer.from_pretrained('mstaron/SingBERTa')

# load the model
model = AutoModelForMaskedLM.from_pretrained("mstaron/SingBERTa")

# import the feature extraction pipeline
from transformers import pipeline

# create the pipeline, which will extract the embedding vectors
# the models are already pre-defined, so we do not need to train anything here
features = pipeline(
    "feature-extraction",
    model=model,
    tokenizer=tokenizer, 
    return_tensor = False
)

# extract the features == embeddings
lstFeatures = features('Class SingletonX1')

# print the first token's embedding [CLS]
# which is also a good approximation of the whole sentence embedding
# the same as using np.mean(lstFeatures[0], axis=0)
lstFeatures[0][0]

# This test checks that the model has been downloaded 
# and that it correctly embeds the text "Test"
# To do that, it uses the embedding vector stored previously in the 
# json file
def test_features():

    # get the embeddings of the word "Test"
    lstFeatures = features("Test")

    # read the oracle from the json file
    with open('test.json', 'r') as f:
        lstEmbeddings = json.load(f)
    
    # assert that the embeddings and the oracle are the same
    assert lstFeatures[0][0] == lstEmbeddings