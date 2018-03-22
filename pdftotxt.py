import os
import pdfminer.pdfparser
import pdfminer.pdfinterp
import pdfminer.converter
import pdfminer.layout


def converter():
    docus=os.listdir(r'original/')
    for d in docus:
        path='original/'+d
        f=open(path,'rb')
        parser=PDFParser(f)
        doc=PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize()
        rsrcmgr=PDFResourceManager()
        laparams=LAParams()
        device=PDFPageAggregator(rsrcmgr,laparams=laparams)
        interpreter=PDFPageInterpreter(rsrcmgr,device)
        for page in doc.get_pages:
            interpreter.process_page(page)
            layout=device.get_result()
            for x in layout:
                if(isinstance(x,LTextBoxHorizonal)):
                    with open(r'666/'+d.replace('.pdf','')+'.txt','a') as ff:
                        result=x_get_text()
                        f.write(result)




