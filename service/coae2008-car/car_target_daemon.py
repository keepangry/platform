#-*- coding: utf-8 -*-
from configure import *
from socket import *
import jieba
import jieba.posseg as pseg
import json
import os
from func0317 import *
import subprocess
import CRFPP



BASE_PATH = os.getcwd()+'/'
TEMP_PATH = BASE_PATH+'tmp/'
MODEL_PATH = BASE_PATH+'output/model'
CRF_TEST = '/usr/local/bin/crf_test'

car_word_jieba_path = BASE_PATH+'output/car_word_jieba'
#加载领域词库，TODO，应该标注词库的词性，默认名词可以
jieba.load_userdict(car_word_jieba_path)

tagger = CRFPP.Tagger("-m "+MODEL_PATH+" -v 3 -n2")

#\n 替换值，这个值应该是词库里的一个非常高频的词，目的作为分隔符
NDEL='豢魧'

def jieba_cut(text):
    words = pseg.cut(text)
    seg_list = []
    for w in words:
        seg_list.append([w.word, w.flag])
    return seg_list

def crf_test(text):
    tagger.clear()
    seg_list = jieba_cut(text.strip())
    for line in seg_list:
        l =  ' '.join(line)+' 1'
        #add不能接受unicode
        tagger.add(l.encode('utf-8'))

    size = tagger.size()
    xsize = tagger.xsize()
    ysize = tagger.ysize()

    tagger.parse()

    #tagger.y2(i)就是预测的结果
    ret_data = []
    for i in range(0, (size - 1)):
        ret_data.append([tagger.x(i, 0),tagger.y2(i)])
    return ret_data


#文章内容生成crf格式数据
def generate_crf_data(text):
    #因为生成crf文件中\n有其特殊含义，所以，字符中不应有\n，把\r or \n replace为\\n
    text = text.replace('\r',NDEL).replace('\n',NDEL)

    #对text进行替换

    tempfile = TEMP_PATH+get_temp_filename()
    seg_list = jieba_cut(text)
    predict_list = []
    for item in seg_list:
        predict_list.append('\t'.join([item[0],item[1],'O']))
    list_to_file(predict_list,tempfile)
    return tempfile


def get_crf_result(test_file):
    #crf_test  -m model test.data
    cmd = [CRF_TEST,'-m '+MODEL_PATH,test_file]
    retcode = os.popen(' '.join(cmd))
    result = retcode.read()
    
    result = result.strip().split('\n')

    #二维列表，带标注结果 0为词，1为O表示不知道，B为评价对象
    ret_data = []
    for line in result:
        line = line.split('\t')
        if len(line)==4:
            ret_data.append([line[0].replace(NDEL,'\n'),line[3]])
    return ret_data


def main():
    HOST='localhost'
    PORT=20317
    BUFSIZ=1024000
    ADDR=(HOST, PORT)
    sock=socket(AF_INET, SOCK_STREAM)
    sock.bind(ADDR)

    sock.listen(5)
    while True:
        tcpClientSock, addr=sock.accept()
        try:
            data=tcpClientSock.recv(BUFSIZ)

            #文件为中间结果方式
            #test_data = generate_crf_data(data)
            #result = get_crf_result(test_data)

            #python直接调用crf方式
            result = crf_test(data)

            result = {"data":result,'status':0}
            tcpClientSock.send(json.dumps(result).encode("utf-8"))
        except:
            tcpClientSock.close()
    tcpClientSock.close()
    sock.close()

main()
