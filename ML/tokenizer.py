import nltk
from nltk.tokenize import word_tokenize

# Ensure necessary NLTK resources are downloaded
# nltk.download('punkt_tab')

# Sample text
text = "Machine learning is amazing!"

# Word tokenization
try:
    tokens = word_tokenize(text)
    print("Tokenized words:", tokens)
except Exception as e:
    print("An error occurred:", e)
