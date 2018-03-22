import pdftotxt
from tokenizer import tokenizer
from analyzer import analyzer
from conclusion import conclusions
import os


pdftotxt.converter()
listd=os.listdir(r'666/')
for f in listd:
    count=1
    path='666/'+f
    token=tokenizer()
    analyze=analyzer()
    con=conclusions()
    token.tokenize(path)
    listt=token.getwords()
    analyze.analyze(listt)
    s=analyze.getResult()
    con.conclude(s,count)
    con.writefile("conclusion.txt")
    count+=1
