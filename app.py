from flask import Flask, request, jsonify, redirect, url_for

import torch
from torch.nn import functional
from gensim.models import Word2Vec

app = Flask(__name__, static_url_path='', static_folder='static')

# 加载模型
model = Word2Vec.load("model/word2vec.model")


@app.route('/')
def index():
    return redirect('index.html')

@app.route('/game', methods=['POST'])
def game():
    if request.method == 'POST':
        element1 = request.form['element1']
        element2 = request.form['element2']
        # # 查询相近的词
        element1_similar_words = [word for word, similarity in model.wv.most_similar(element1, topn=1000)]
        element2_similar_words = [word for word, similarity in model.wv.most_similar(element2, topn=1000)]
        similar_word = find_first_common_word(element1_similar_words,element2_similar_words)
        print(similar_word)
        return similar_word
    else:
        return app.send_static_file('login.html')

def find_first_common_word(list1, list2):

    # 遍历第二个列表，检查每个单词是否在第一个列表中出现过
    for word1 in list1:
        for word2 in list2:
            if word1 == word2:
                return word1

    # 如果没有找到相同的单词，返回None
    return None

if __name__ == '__main__':
    app.run(port=5000)
