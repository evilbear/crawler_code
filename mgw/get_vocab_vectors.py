import os
import shutil
import word2vec

###蒙语做词频和词向量时，先把(窄的无中断空格 U+202F)替换成空格，优化单词稀疏问题
###把data语料转换成data_用于词频和词向量
def del_space(data_path, save_path):
    data_file = open(data_path, "r")
    save_file = open(save_path, "w")
    for line in data_file:
        for i in line:
            if i == ' ':#此处是U+202F
                save_file.write(' '+i)#此处是空格
            else:
                save_file.write(i)
    data_file.close()
    save_file.close()

###计算词频和词向量,词向量有glove和word2vec训练出来的两类
def create():
    data_path_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data_.txt'
    glove_data = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/code/GloVe-master/data_.txt'
    shutil.copyfile(data_path_,glove_data)
    os.system("cd GloVe-master;sh demo.sh")
    os.remove(glove_data)
    os.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/code/GloVe-master/vectors.bin')
    if not os.path.exists(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/vectors'):
        os.mkdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/vectors')
    shutil.move( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/code/GloVe-master/vectors.txt', os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/vectors/glove_vectors.txt')
    shutil.move( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/code/GloVe-master/vocab.txt', os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/vocab.txt')
    word2vec.word2vec(data_path_, os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/vectors/word2vec_vectors.txt', size=300, verbose=True, binary=0, min_count=5)

    
    
    
    
data_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data.txt'
data_path_ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data_.txt'
data_size = os.path.getsize(data_path)
if os.path.exists(data_path_):
    data_size_ = os.path.getsize(data_path_)
    if data_size > data_size_*1.1:#当更新量大于10%时，重新计算词频和词向量
        del_space(data_path,data_path_)
        create()
    else:
        pass
else:
    del_space(data_path,data_path_)
    create()

