import sys
sys.path.append('..')
import os
from gensim import corpora, models
from conf.trainModel_conf import path_dictionary, path_tmp_lsi, path_tmp_lsimodel, path_tmp_predictor
import pickle as pkl
import jieba
from scipy.sparse import csr_matrix

def predict(doc):
    files = os.listdir(path_tmp_lsi)
    dictionary = corpora.Dictionary.load(path_dictionary)
    lsi_file = open(path_tmp_lsimodel, 'rb')
    lsi_model = pkl.load(lsi_file)
    lsi_file.close()
    x = open(path_tmp_predictor, 'rb')
    predictor = pkl.load(x)
    x.close()
    catg_list = []
    for file in files:
        t = file.split('.')[0]
        if t not in catg_list:
            catg_list.append(t)

    demo_doc = list(jieba.cut(doc, cut_all=False))
    demo_bow = dictionary.doc2bow(demo_doc)
    tfidf_model = models.TfidfModel(dictionary=dictionary)
    demo_tfidf = tfidf_model[demo_bow]
    demo_lsi = lsi_model[demo_tfidf]
    data = []
    cols = []
    rows = []
    for item in demo_lsi:
        data.append(item[1])
        cols.append(item[0])
        rows.append(0)
    demo_matrix = csr_matrix((data, (rows, cols))).toarray()
    x = predictor.predict(demo_matrix)
    p = predictor.predict_proba(demo_matrix)
    for i in range(4):
        print("类别{c}歌曲分类概率为: {p}".format(c=catg_list[i],p=p[0][i]))
    return catg_list[x[0]]

if __name__ == '__main__':
    doc = """
    我有一个好爸爸
    """
    print(predict(doc))