#-*- coding: utf-8 -*-
from socket import *
import jieba
import json

HOST='localhost'
PORT=2012
BUFSIZ=10240
ADDR=(HOST, PORT)
sock=socket(AF_INET, SOCK_STREAM)
sock.bind(ADDR)

sock.listen(5)
while True:
    tcpClientSock, addr=sock.accept()
    try:
        #print "1"
        #exit()
        data=tcpClientSock.recv(BUFSIZ)
        jieba_res = " ".join(jieba.cut(data,cut_all=False))
        result = {"data":jieba_res}
        tcpClientSock.send(json.dumps(result).encode("utf-8"))
    except:
        tcpClientSock.close()
tcpClientSock.close()
sock.close()
