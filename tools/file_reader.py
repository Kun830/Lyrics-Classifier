import os


class loadFolders(object):   # 迭代器
    def __init__(self, par_path):
        self.par_path = par_path

    def __iter__(self):
        for file in os.listdir(self.par_path):
            file_abspath = os.path.join(self.par_path, file)
            if os.path.isdir(file_abspath):  # if file is a folder
                yield file_abspath


class loadFiles(object):
    def __init__(self, par_path):
        self.par_path = par_path

    def __iter__(self):
        folders = loadFolders(self.par_path)
        for folder in folders:              #爬取歌词种类目录
            catg = folder.split(os.sep)[-1]
            for file in os.listdir(folder):     #迭代每种种类歌词的每首歌
                file_path = os.path.join(folder, file)
                if os.path.isfile(file_path):
                    this_file = open(file_path, 'rb')
                    content = this_file.read().decode('utf8')
                    yield catg, content
                    this_file.close()