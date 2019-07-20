from gensim.models import word2vec
model = word2vec.Word2Vec.load('saved_model/toji.model')
content = model.most_similar(positive=["집"])
print(content)