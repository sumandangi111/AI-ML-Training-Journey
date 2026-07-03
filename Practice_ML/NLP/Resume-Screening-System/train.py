from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("job_description.txt","r") as file:
    jd=file.read()

with open("resume1.txt","r") as file:
    resume1=file.read()

with open("resume2.txt","r") as file:
    resume2=file.read()

documents=[
    jd,
    resume1,
    resume2
]

vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(documents)
similarity=cosine_similarity(X)
print(similarity)
print("Resume 1 Match:", similarity[0][1])
print("Resume 2 Match:", similarity[0][2])