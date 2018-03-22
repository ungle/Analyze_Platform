import pymysql
from collections import Counter

class analyzer:

    def __init__(self):
        self.__analyzeResult=""

    def analyze(self,list):
        file=open("specialwords.txt",'r',encoding="utf-8") #打开特征词文件
        specialwords=[]
        for line in file:
            line=line.strip()
            line=str(line)
            specialwords.append(line)

        cnt=Counter()
        for w in list:
            if w in specialwords: #统计词频
                cnt[w]+=1

        gaopin=cnt.most_common(3) 
        conn=pymysql.connect(host='127.0.0.1',port=3306,user='client',passwd='23333',db='sp',charset='utf8') #连接数据库
        curser=conn.cursor()

        for g in gaopin:
            k=str(g[0])
            curser.execute("select theme,subtheme,feature_word,object from theme_pattern where feature_word='"+k+"' or object='"+k+"'") #查询贡献
            row1=curser.fetchone()
            self.__analyzeResult=self.__analyzeResult+str(row1)+" "

        self.__analyzeResult="这篇论文的贡献在于："+self.__analyzeResult
        file.close()
        
    def getResult(self):
        return self.__analyzeResult




     
    
    