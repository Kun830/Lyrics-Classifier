import os

path_doc_root = '../data'  # 根目录 即存放按类分类好的问本纪
path_tmp = '../model/'  # 存放中间结果及模型的位置
path_dictionary = os.path.join(path_tmp, 'WangYiMusic.dict')  # 存放字典
path_tmp_tfidf = os.path.join(path_tmp, 'tfidf_corpus')  # 存放tfidf语料库
path_tmp_lsi = os.path.join(path_tmp, 'lsi_corpus')  # 存放lsi语料库
path_tmp_lsimodel = os.path.join(path_tmp, 'lsi_model.pkl')  # 存放lsi模型
path_tmp_predictor = os.path.join(path_tmp, 'predictor.pkl')  # 存放训练好的模型