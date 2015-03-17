#encoding=utf8
from func0317 import *
from configure import *
import os

#encoding=utf8
class Crf(object):
    """docstring for Crf"""
    def __init__(self):
        super(Crf, self).__init__()
        self.crf_data_path = BASE_PATH+'output/crf_data'
        self.train_data_path = BASE_PATH+'output/train_data'
        self.test_data_path = BASE_PATH+'output/test_data'
        self.test_result_path = BASE_PATH+'output/test_result'

        self.model_path = BASE_PATH+'output/model'
        self.template_path = BASE_PATH+'template'

        self.split_train_test()


    #rate为训语料练占总数的比例
    def split_train_test(self,rate=0.7,seed='crf'):
        import random
        random.seed(seed)
        self.article_list = crf_to_1list(self.crf_data_path)
        random.shuffle(self.article_list)
        count = len(self.article_list)
        sep_i = int(rate*count)
        self.train_list = self.article_list[:sep_i]
        self.test_list = self.article_list[sep_i:]
        crf1list_to_file(self.train_list,self.train_data_path)
        crf1list_to_file(self.test_list,self.test_data_path)

    def train(self):
        #crf_learn -c 10.0 template train.data model
        cmd = ['crf_learn','-c 10.0',self.template_path,self.train_data_path,self.model_path]
        os.system(' '.join(cmd))

    def test(self):
        #crf_test  -m model test.data
        cmd = ['crf_test','-m '+self.model_path,self.test_data_path,'>'+self.test_result_path]
        os.system(' '.join(cmd))

    def get_prf(self):
        #检测预测结果文件是否存在
        if not os.path.exists(self.test_result_path):
            print '错误！ 预测文件'+self.test_result_path+'不存在，请先进行crf test'
            return

        label = 0
        predict = 0
        hit = 0
        with open(self.test_result_path) as f:
            for line in f:
                line = line.strip().split('\t')
                if len(line)==4:
                    if line[2]=='B':
                        label += 1
                        if line[3]=='B':
                            hit += 1
                    if line[3]=='B':
                        predict += 1
        precision = float(hit) / predict
        recall = float(hit) / label
        f1 = 2*precision*recall / float(precision+recall)

        print 'label: '+str(label)
        print 'predict: '+str(predict)
        print 'hit: '+str(hit)
        print 'precision: '+str(precision)
        print 'recall: '+str(recall)
        print 'f1: '+str(f1)



crf = Crf()
crf.train()
crf.test()
crf.get_prf()
