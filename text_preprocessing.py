import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
class textpreprocessing:
    def __init__(self,input_file_path):
        with open(input_file_path,'r') as f:
            nda_text=f.read()
            tokens = nltk.word_tokenize(nda_text)
            print(tokens)
            clean_tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
            print(clean_tokens)
            stop_words = set(stopwords.words('english'))
            filtered_tokens = [token for token in clean_tokens if not token in stop_words]
            print(filtered_tokens)
            stemmer = PorterStemmer()
            normalized_tokens = [stemmer.stem(token.lower()) for token in filtered_tokens]
            print(normalized_tokens)
    def preprocess_text(text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9]", " ", text)
        tokens = nltk.word_tokenize(text)
        encoded_tokens = [i for i, word in enumerate(tokens)]
        padded_tokens = encoded_tokens[:1024]
        padded_tokens += [0] * (1024 - len(padded_tokens))
        return padded_tokens

    # for example in ndas:
    #     example["prompt"] = preprocess_text(example["prompt"])
    #     example["output"] = preprocess_text(example["output"])