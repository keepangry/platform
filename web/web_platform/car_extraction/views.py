#encoding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
import os

# Create your views here.
def opinion_target(req):
    template = loader.get_template('opinion_target.html')

    import subprocess
    p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    line = "".join(p.stdout.readlines())

    name = "haha"
    context = Context({
        'name':name,
        'title':line,
    })
    return HttpResponse(template.render(context))

def observe_car(req):
    template = loader.get_template('observe_car.html')
    crf_data_path = os.getcwd()+'/data/crf_data'

    data = []
    with open(crf_data_path) as f:
        texts = f.read().strip().split('\n\n')

    for text in texts:
        content = []
        for line in text.strip().split('\n'):
            line_l = line.split('\t')
            content.append([line_l[0],line_l[-1]])
        data.append(content)


    # for text in texts:
    #     content = ""
    #     for line in text.strip().split('\n'):
    #         line_l = line.split('\t')
    #         if line[-1]=="B":
    #             content += '['+line_l[0]+'] '
    #         else:
    #             content += line_l[0]+' '
    #     data.append(content)
    
    line = ""
    context = Context({
        'title':line,
        'data':data,
        #'data1':data1,
    })

    return HttpResponse(template.render(context))