#encoding=utf8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
import jieba
from django.template import Context, loader
import os
import sys


def get_jieba_socket(content,result):
    from socket import *
    HOST='localhost'
    PORT=20317
    BUFSIZ=1024000
    ADDR=(HOST, PORT)
    client=socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)

    if sys.getsizeof(content)>BUFSIZ:
        result['status'] = -1
        result['info'] = '文本内容过长'
        return False

    client.send(content)
    data=client.recv(BUFSIZ)
    
    ret = json.loads(data)
    if ret['status']==0:
        result['status'] = 0
        result['info'] = "success"
        result['data'] = ret['data']

    return True

# Create your views here.
def segmentation(req):
    content = req.POST['content'].strip()
    result = {"status":-1, "data":"", "info":"失败"}
    get_jieba_socket(content,result)

    return HttpResponse(json.dumps(result), content_type="application/json")
