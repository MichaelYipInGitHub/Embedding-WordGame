from gensim.models import Word2Vec

# 加载模型
model = Word2Vec.load("model/word2vec.model")
#
# # 查询相近的词
word1 = "wind"
word1_similar_words = [word for word, similarity in model.wv.most_similar(word1, topn=1000)]
word2 = "plant"
word2_similar_words = [word for word, similarity in model.wv.most_similar(word2, topn=1000)]

def find_first_common_word(list1, list2):

    # 遍历第二个列表，检查每个单词是否在第一个列表中出现过
    for word1 in list1:
        for word2 in list2:
            if word1 == word2:
                return word1

    # 如果没有找到相同的单词，返回None
    return None

print(find_first_common_word(word1_similar_words,word2_similar_words))
