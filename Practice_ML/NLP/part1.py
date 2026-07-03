# Text preprocessing and tokenization

# text="Python, Machine Learning, Flask."
# print(text)
# print("original----------")

# text=text.lower()
# text=text.replace(",","")
# text=text.replace(".","")
# print()

# print("After Cleaning:")
# print(text)
# words=text.split()
# print()
# print(words)

# text="I have experience in Python, SQL, Java, Machine Learning and Flask."
# text=text.lower()
# text=text.replace(",","")
# text=text.replace(".","")
# words=text.split()
# print()
# print(words)

# filtered_words=[]
# for word in words:
#     if not (word=="i" or word=="have" or word=="in" or word=="and" or word=="the" or word=="is" or word=="are" or word=="to"  or word=="of"):
#         filtered_words.append(word)
# print(filtered_words)

# words=['python','sql','flask','java']
# sentence1 = "python sql flask"
# l1=[]
# count1=0
# sentence2 = "python java sql"
# l2=[]
# count2=0
# for word in words:
#     if word in sentence1:
#         l1.append(words.count(word))
# for word in words:
#     if word in sentence2:
#         l2.append(words.count(word))
# print(l1)
# print(l2)

# Bag of Words
# from sklearn.feature_extraction.text import CountVectorizer

# documents = [
#     "python sql flask",
#     "python java sql"
# ]

# vectorizer = CountVectorizer()

# X = vectorizer.fit_transform(documents)

# print(vectorizer.get_feature_names_out())
# print(X.toarray())


# TF-IDF
# from sklearn.feature_extraction.text import TfidfVectorizer

# documents = [
#     "python sql flask",
#     "python java sql"
# ]

# vectorizer = TfidfVectorizer()

# X = vectorizer.fit_transform(documents)

# print(vectorizer.get_feature_names_out())
# print(X.toarray())


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "python sql flask",      # Job Description
    "python sql flask",      # Resume 1
    "java html css"          # Resume 2
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

similarity = cosine_similarity(X)

print(similarity)