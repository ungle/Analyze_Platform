import jieba
import os

class tokenizer:
    
    def __init__(self):
        jieba.load_userdict('userdict.txt') #载入用户词典
        self.__words=[]

    def tokenize(self,path):
        file=open(path,'r',encoding="utf-8")
        lines=[]
        for line in file:
            line=line.strip()
            line=str(line)
            lines.append(line)
        data=''.join(lines)
        w=jieba.cut(data) #分词
        for k in w:
            self.__words.append(k)

    def getwords(self):
        return self.__words


