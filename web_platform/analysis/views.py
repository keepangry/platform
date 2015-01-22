#encoding=utf8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
import jieba
from django.template import Context, loader
import os

# Create your views here.
def segmentation(req):
    content = req.POST['content']
    jieba_res = jieba.cut(content,cut_all=False)
    result = {"status":0, "data":"", "info":""}
    seg_result = " ".join(jieba_res)
    result['data'] = seg_result

    return HttpResponse(json.dumps(result), content_type="application/json")
