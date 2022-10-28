import spacy
# https://www.projectpro.io/recipes/install-and-use-spacy-models
nlp = spacy.load("en_core_web_sm")

def text_processing(sentence):
    """
    Lemmatize, lowercase, remove numbers and stop words
    
    Args:
      sentence: The sentence we want to process.
    
    Returns:
      A list of processed words
    """
    sentence = [token.lemma_.lower()
                for token in nlp(sentence) 
                if token.is_alpha and not token.is_stop]
    
    return sentence

#sentence = "This is a test sentence to check if this is working correctly."
#print(text_processing(sentence))