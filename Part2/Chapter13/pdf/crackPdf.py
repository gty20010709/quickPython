import PyPDF2

with open('dictionary.txt', 'r') as f:
    CassList = f.readlines()

pw_ls = []
for CPW in CassList:
    pw_ls.append(CPW)
    pw_ls.append(CPW.lower())

with open('encrypted.pdf', 'rb') as pdf:
    pdfReader = PyPDF2.PdfReader(pdf)
    for pw in pw_ls:
        if False == pdfReader.decrypt(pw):
            print('False')

    # if pdfReader.isEncrypted:
        # print('Encrypted')
