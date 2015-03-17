#encoding=utf8
#from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
import json
#import jieba
#from django.template import Context, loader
import os

from socket import *

def get_jieba_socket(content):
    HOST='localhost'
    PORT=20318
    BUFSIZ=10240
    ADDR=(HOST, PORT)
    client=socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    client.send(content)
    data=client.recv(BUFSIZ)
    result = json.loads(data.decode('utf8'))
    return result['data']

# Create your views here.
def segmentation():
    content = u"将内能转化成动能的机构称之为发动机，汽车发动机的形式主要是以气缸和活塞作为转换机构的内燃机。根据燃料以及点火形式的不同可分为汽油机或柴油机，或有以氢气、天然气、石油气为燃料的发动机，其燃烧形式与汽油机差异较小。根据工作循环与活塞冲程特性划分，又可分为两冲程与四冲程发动机，本网站涉及的汽车发动机主要是四冲程汽油机或四冲程柴油机。"
    client=get_jieba_socket(content.encode('utf8'))
    #jieba_res = jieba.cut(content,cut_all=False)
    #seg_result = " ".join(jieba_res)
    result = {"status":0, "data":"", "info":""}
    #print client
    result['data'] = client
    print json.dumps(result)

    #return HttpResponse(json.dumps(result), content_type="application/json")

segmentation()
