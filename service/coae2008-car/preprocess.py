#encoding=utf8
from configure import *
from func0317 import *
import jieba
import jieba.posseg as pseg

class CarCrf:
    def init(self):
        self.answer_path = BASE_PATH+'source/answer_all.txt'
        self.car_path = BASE_PATH+'source/Car/'
        self.car_word_jieba_path = BASE_PATH+'output/car_word_jieba'

        self.car_dict = {}
        self.all_crf_data = {}

        self.get_car_dict()
        self.put_answer_to_car_dict()
        self.genete_jieba_dict()
        #加载词库
        jieba.load_userdict(self.car_word_jieba_path)

        #self.generate_crf(self.car_dict[self.car_dict.keys()[0]])
        self.get_all_car_crf_list()
        print "ok"
        self.write_to_file1()
        print "write ok"
        


    def get_all_car_crf_list(self):
        for key in self.car_dict.keys():
            self.all_crf_data[key] = self.get_one_car_crf_list(self.car_dict[key]) 
        return True


    def write_to_file(self):
        all_crf_data_list = []
        for key in self.all_crf_data.keys():
            if len(self.all_crf_data[key])>0:
                for line_l in self.all_crf_data[key]:
                    if len(line_l[0].strip())>0:
                        all_crf_data_list.append('\t'.join(line_l))
                all_crf_data_list.append('\n')
        list_to_file(all_crf_data_list,BASE_PATH+'output/crf_data')
        
    def write_to_file1(self):
        all_crf_data_list = []
        for key in self.all_crf_data.keys():
            if len(self.all_crf_data[key])>0:
                for line_l in self.all_crf_data[key]:
                    if len(line_l[0].strip())>0:
                        all_crf_data_list.append(line_l)
                #不同文章间空一行
                all_crf_data_list.append([''])
        list2v_to_file(all_crf_data_list,BASE_PATH+'output/crf_data')

    def get_one_car_crf_list(self,car_data):
        text = car_data['text']
        text_seg = self.jieba_cut(text)
        answer = car_data['answer']
        crf_data = []
        #for w_index in car_data['answer']:
        index = 0
        max = len(answer)
        if max == 0 :
            return crf_data
        
        current = answer[index]
        count = 0
        for item in text_seg:
            count += len(item[0])
            crf_data.append([item[0],item[1],'O'])
            if count >= current[0]:
                #print item[0]
                crf_data[-1][2] = 'B'
                index += 1
                if index < max:
                    current = answer[index]
                else:
                    current = [10000000,0]
        return crf_data
                    

                

        #print text_seg


    def jieba_cut(self,text):
        words = pseg.cut(text)
        seg_list = []
        for w in words:
            seg_list.append([w.word, w.flag])
        return seg_list


    #依赖self.get_car_dict
    #获取答案数据
    def put_answer_to_car_dict(self):
        answer_list = read_to_list(self.answer_path)
        for line in answer_list:
            line = line.split('\t')
            key = line[1]
            if key in self.car_dict:
                self.car_dict[key]['answer'].append(map(lambda x:int(x),line[2:]))

    #获取car数据，并放入词典
    #key为id,value为{'text':value,'answer':[]}
    def get_car_dict(self):
        files = get_all_files(self.car_path)
        car_data = map(self.car_file_parse,files)
        for item in car_data:
            #key = item['DOCID'].split('_')[1]
            key = item['DOCID']
            self.car_dict[key] = {'text':item['TEXT'],'file':item['file'],'answer':[]}

    #解析某个car文件
    def car_file_parse(self,file_path):
        content = file(file_path).read().strip()
        filename = os.path.basename(file_path)
        data = xml_to_dict(content)['DOC']
        data['file'] = filename
        return data

    #under self.put_answer_to_car_dict
    #获取确定分词
    def get_ensure_word(self):
        data = []
        for key in self.car_dict.keys():
            text = self.car_dict[key]['text']
            for i in self.car_dict[key]['answer']:
                #因为标注是从1开始，故减一
                data.append([text[i[0]-1:i[1]-1],i[0],i[1],key,self.car_dict[key]['file']]) 
        return data

    #从标注中生成词典
    def genete_word_dict(self,filename=''):
        ensure_word_list = self.get_ensure_word()
        word_list = map(lambda x:x[0],ensure_word_list)
        if filename != '':
            list_to_file(word_list,filename)
        return word_list

    #jieba dict
    def genete_jieba_dict(self,my_w=3,coae_w=10):
        my_car_word = read_to_list(BASE_PATH+'/source/my_car_word')
        coae_car_word = read_to_list(COAE_CAR_WORD)
        new_car_word_jieba = []
        for i in my_car_word:
            if i not in coae_car_word:
                new_car_word_jieba.append(i+' '+str(my_w))
        for i in coae_car_word:
            new_car_word_jieba.append(i+' '+str(coae_w))
        list_to_file(new_car_word_jieba,BASE_PATH+'output/car_word_jieba')

        #我的词库
        #dict_to_jieba(BASE_PATH+'/source/my_car_word',BASE_PATH+'/output/my_car_word_jieba')
        #coae2008词库
        #dict_to_jieba(COAE_CAR_WORD,COAE_CAR_WORD+'_jieba',10)

    #生成一段文字的crf特征文件
    #def generate_article_crf_data(self,):
        #return


#car = CarCrf()
#car.init()



#生成词典
#car.genete_word_dict(COAE_CAR_WORD)
