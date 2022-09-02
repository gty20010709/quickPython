import PyPDF2
import os


def getPDF(filename):
    pdf = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdf)
    # pdf.close()
    if pdfReader.isEncrypted:
        return None
    return pdfReader
path = '.'
pdf_ls = []
for filename in os.listdir(path):
    # print(filename)
    if filename.lower().endswith('.pdf'):
        pdf_ls.append(filename)


pdfWriter = PyPDF2.PdfWriter()

# print(pdf_ls)
for filename in pdf_ls:
    # print(getPDF(filename))
    pdfReader = getPDF(filename)
    if pdfReader == None:
        continue
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    
with open('Merged.pdf','wb') as result:
    pdfWriter.write(result)
