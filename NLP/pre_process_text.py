import nltk
nltk.download('stopwords')
nltk.download('punkt')

import re

def pre_process_text(doc, method):
    stop_words = nltk.corpus.stopwords.words('english')

    # lower case and remove special characters\whitespaces
    doc = re.sub(r'[^a-zA-Z\s]', '', doc, flags=re.I|re.A) # [^a-zA-Z\s] => remove any digits, special characters, symbols etc.
    if method == "TF_IDF":
        # include stemming
        # TODO
        pass
    doc = doc.lower()
    doc = doc.strip()
    # tokenize document
    tokens = nltk.word_tokenize(doc)
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)
    return doc

# sentence = "These are two test sentences to check if this is working correctly. We do this 4 social good. "
# print(sentence)
# print(pre_process_text(sentence))