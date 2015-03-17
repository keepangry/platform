#encoding=utf8
from configure import *
import os
import xmltodict
import json
import time
import random
import hashlib


#把文件读入列表
def read_to_list(path,delimiter='\n'):
    with open(path) as f:
        return f.read().strip().decode('utf8').split(delimiter)

#把列表写入文件，默认以\n分割
def list_to_file(l,path,delimiter='\n'):
    with open(path,'w') as f:
        f.write(delimiter.join(l))

def list2v_to_file(l,path,del1='\t',del2='\n'):
    with open(path,'w') as f:
        content = ""
        for i in l:
            content += del1.join(i)
            content += del2
        f.write(content)

#获取目录下所有文件
def get_all_files(path):
    return map(lambda x:path.rstrip('/')+'/'+x,os.listdir(path))




#解析xml
#返回结果为OrderedDict,即有序字典,按加入的顺序算
def xml_to_dict(content_str):
    convertedDict = xmltodict.parse(content_str)
    return convertedDict
    
    jsonStr = json.dumps(convertedDict,ensure_ascii = False)
    return json.loads(jsonStr)


#生成jieba自定义词典需要的格式
def dict_to_jieba(filepath,new_filepath,freq=3):
    dict_list = read_to_list(filepath)
    new_dict_list = []
    for i in dict_list:
        new_dict_list.append(i+' '+str(freq))
    list_to_file(new_dict_list,new_filepath)


#把crf数据按\n\n分割读取到一维列表中
def crf_to_1list(path):
    with open(path) as f:
        return f.read().strip().split('\n\n')

def crf1list_to_file(l,path,delimiter='\n\n'):
    with open(path,'w') as f:
        f.write(delimiter.join(l))        

#获取唯一临时文件名
def get_temp_filename():
    hashstr = str(time.time())+str(random.random())
    tempfile=hashlib.md5(hashstr).hexdigest()+str(random.random())
    return tempfile
