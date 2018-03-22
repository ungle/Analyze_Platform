
class conclusions:

    def __init__(self):
        self.__conclusion=""

    def conclude(self,result,count):
        count=str(count)
        self.__conclusion="第"+count+"篇论文的贡献以及相应特征词和词频是: "+result

    def writefile(self,outputPath):
        file=open(outputPath,'w',encoding="utf-8")
        file.write(self.__conclusion)
        file.write('/n')
        file.close()
