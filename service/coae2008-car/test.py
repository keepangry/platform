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
#print '\t'.join(['1'])
#print '\n\n'