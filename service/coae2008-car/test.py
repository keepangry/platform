#encoding=utf8
def list2v_to_file(l,path,del1='\t',del2='\n'):
    with open(path,'w') as f:
        content = ""
        for i in l:
            #print '1'
            content += del1.join(i)
            #print del1.join(i)
            content += del2
        f.write(content)

a = [['a','b'],[''],['c','d']]

list2v_to_file(a,'test.result')

import sys
a = False
#print sys.getsizeof(a)
#print '\t'.join(['1'])
#print '\n\n'
import jieba
import jieba.posseg as pseg

def jieba_cut(text):
    words = pseg.cut(text)
    seg_list = []
    for w in words:
        seg_list.append([w.word, w.flag])
    return seg_list

a = jieba_cut('\n\n\n')
print a


