# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer(
#     "all-MiniLM-L6-v2"
# )

# sentences = [
#     "Python Developer",
#     "Software Engineer",
#     "Java Developer"
# ]

# embeddings = model.encode(sentences)

# print(embeddings.shape)


from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python Developer",
    "Software Engineer",
    "Java Spring Developer"
]

embeddings = model.encode(sentences)

similarity = cosine_similarity(embeddings)

print(similarity)