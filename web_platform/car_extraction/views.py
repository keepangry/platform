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