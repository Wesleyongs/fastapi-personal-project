from sgnlp.models.sentic_gcn import (
    SenticGCNBertTokenizer,
    SenticGCNBertEmbeddingConfig,
    SenticGCNBertEmbeddingModel,
    SenticGCNBertModel,
    SenticGCNBertPreprocessor,
    SenticGCNBertConfig,
    SenticGCNBertPostprocessor,
)
import datetime as dt
import os

import spacy
from dotenv import load_dotenv

import src.routes.nlphub.models as models

load_dotenv()


""" # Create tokenizer
tokenizer = SenticGCNBertTokenizer.from_pretrained("bert-base-uncased")

# Create embedding model
embed_config = SenticGCNBertEmbeddingConfig.from_pretrained(
    "bert-base-uncased")
embed_model = SenticGCNBertEmbeddingModel.from_pretrained(
    "bert-base-uncased", config=embed_config)

# Create preprocessor
preprocessor = SenticGCNBertPreprocessor(
    tokenizer=tokenizer,
    embedding_model=embed_model,
    senticnet="https://storage.googleapis.com/sgnlp/models/sentic_gcn/senticnet.pickle",
    device="cpu",
)

# Create postprocessor
postprocessor = SenticGCNBertPostprocessor()

# Load model
config = SenticGCNBertConfig.from_pretrained(
    "https://storage.googleapis.com/sgnlp/models/sentic_gcn/senticgcn_bert/config.json"
)

model = SenticGCNBertModel.from_pretrained(
    "https://storage.googleapis.com/sgnlp/models/sentic_gcn/senticgcn_bert/pytorch_model.bin", config=config
)

nlp = spacy.load("en_core_web_md") """


def get_nouns(sentence):

    # Load the large English NLP model
    doc = nlp(sentence)

    aspects = set()
    for token in doc:
        #         if token.pos_ == "NOUN" and any([child.pos_ == "ADJ" for child in token.children]):
        if token.pos_ == "NOUN" or token.pos_ == "VERB":
            aspects.add(token.text)
    return list(aspects)


def format_input_for_nlp_hub(sentence_array):

    return [{"aspects": get_nouns(i), "sentence": i} for i in sentence_array]


def run_nlp_hub(inputs):
    processed_inputs, processed_indices = preprocessor(inputs)
    outputs = model(processed_indices)

    # Postprocessing
    post_outputs = postprocessor(
        processed_inputs=processed_inputs, model_outputs=outputs)
    return post_outputs


def get_sentiments(inputs):
    try:
        res = run_nlp_hub(format_input_for_nlp_hub(inputs))
    #     return [ " ".join(i['sentence']) for i in res ]
        return [sum(i['labels']) > 0 for i in res]
    except:
        return ["something went wrong with"]
