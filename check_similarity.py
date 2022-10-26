from sentence_transformers import CrossEncoder

def check_similarity(text_1, text_2):
    # TODO: https://towardsdatascience.com/semantic-textual-similarity-83b3ca4a840e
    if text_1 == text_2:
        return 1
    else:
        return 0.1

# Load the pre-trained model
model = CrossEncoder('cross-encoder/stsb-roberta-base')

sentence_pairs = []
for sentence1, sentence2 in zip(stsb_test['sentence1'], stsb_test['sentence2']):
    sentence_pairs.append([sentence1, sentence2])
    
stsb_test['SBERT CrossEncoder_score'] = model.predict(sentence_pairs, show_progress_bar=True)
