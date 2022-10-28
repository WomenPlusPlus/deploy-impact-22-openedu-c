from sentence_transformers import CrossEncoder
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from cos_sim import cos_sim

# from text_processing import text_processing

def check_similarity(text_1, text_2):
    # TODO: https://towardsdatascience.com/semantic-textual-similarity-83b3ca4a840e
    
    # tokenize the sentences
    # text_1 = text_processing(text_1)
    # text_2 = text_processing(text_2)

    print(text_1)
    print(text_2)

    # Load the pre-trained model
    method = "BI_ENCODER"

    if method == "CROSS_ENCODER":
        model = CrossEncoder('cross-encoder/stsb-roberta-base')
        similarity_score = model.predict([text_1, text_2], show_progress_bar=True)
        print(similarity_score)
        return similarity_score

    elif method == "BI_ENCODER":
        # Load the pre-trained model
        model = SentenceTransformer('stsb-mpnet-base-v2')
        # Generate Embeddings
        sentence1_emb = model.encode(text_1, show_progress_bar=True)
        sentence2_emb = model.encode(text_2, show_progress_bar=True)

        # Cosine Similarity
        similarity_score = cosine_similarity(sentence1_emb.reshape(1,-1), sentence2_emb.reshape(1,-1))[0][0]
        print(similarity_score)
        return similarity_score


text_1 = "Our earth is round."
text_2 = "The globe is spherical."
check_similarity(text_1, text_2)

text_3 = "The cat sits outside."
text_4 = "The new movie is so great."
check_similarity(text_3, text_4)

