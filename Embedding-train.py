import requests
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# 下载数据
url = "https://realworldnlpbook.s3.amazonaws.com/data/text8/text8"
response = requests.get(url)
with open('text8', 'w') as f:
    f.write(response.text)

# 读取数据
sentences = LineSentence('text8')

# 训练模型
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# 保存模型
model.save("model/word2vec.model")
