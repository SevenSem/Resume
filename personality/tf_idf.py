
import PyPDF2  
import os.path 
pdfFileObj = open('Doc1.pdf', 'rb')  
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
print(pdfReader.numPages)  
pageObj = pdfReader.getPage(0)  
print(pageObj.extractText())  
pdfFileObj.close()
