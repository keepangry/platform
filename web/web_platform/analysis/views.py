#encoding=utf8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
import jieba
from django.template import Context, loader
import os


def get_jieba_socket(content):
    from socket import *
    HOST='localhost'
    PORT=2012
    BUFSIZ=10240
    ADDR=(HOST, PORT)
    client=socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    client.send(content)
    data=client.recv(BUFSIZ)
    result = json.loads(data.decode('utf8'))
    return result['data']

# Create your views here.
def segmentation(req):
    content = req.POST['content']
    client=get_jieba_socket(content.encode('utf8'))
    #jieba_res = jieba.cut(content,cut_all=False)
    #seg_result = " ".join(jieba_res)
    result = {"status":0, "data":"", "info":""}
    result['data'] = client

    return HttpResponse(json.dumps(result), content_type="application/json")
