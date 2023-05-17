import spacy
from spacy_download import load_spacy

# Load the pre-trained NER model from spaCy
# nlp = spacy.load("en_core_web_sm")
nlp = load_spacy("en_core_web_sm", exclude=["parser", "tagger"]) 

# Example text to be analyzed
text = "Apple is looking at buying U.K. startup for $1 billion"

# Parse the text using spaCy NER model
doc = nlp(text)

# Extract named entities from the document
for ent in doc.ents:
    print(ent.text, ent.label_)
