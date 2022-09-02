# mcb.py(w) - Saves and loads pieces of text to the clipboard.
# Usage:
#    mcb.py save <keyword> - Saves clipboard to keyword.
#    mcb.py <keyword> - Loads keyword to clipword.
#    mcb.py list - Loads all keywords to clipboard.
#    mcb.py del - Delete all keywords from clipboard.
#    mcy.py del <keywordd> - Delete keyword from clipboard.

import pyperclip
import sys
import shelve

para = sys.argv[1:]

def saveSnip(keyword,content):
    fileObj = shelve.open('mcb.shelve')
    fileObj[keyword] = content
    fileObj.close()

def loadSnip(keyword):
    fileObj = shelve.open('mcb.shelve')
    content = fileObj[keyword]
    fileObj.close()
    return content

def loadAllSnips():
    fileObj = shelve.open('mcb.shelve')
    contentLs = list(fileObj.items())
    contentTitle = f'{"KEYWORDS".rjust(15)}      CONTENT\n' + '\n'
    string = ''
    for key,value in contentLs:
        string += f'{key.rjust(15)}     {value}' + '\n'
    content = contentTitle + string
    fileObj.close()
    return content

def deleteSnips(keyword):
    fileObj = shelve.open('mcb.shelve')
    del fileObj[keyword]
    fileObj.close()


def deleteAllSnips():
    fileObj = shelve.open('mcb.shelve')
    fileObj.clear()
    fileObj.close()

if len(para) == 2 and para[0] == 'save':
    keyword = para[1]
    content = pyperclip.paste()
    saveSnip(keyword,content)

elif len(para) == 2 and para[0] == 'del':
    keyword = para[1]
    deleteSnips(keyword)
    print(f'Delete snip named: {keyword}')

elif len(para) == 1:
    if para[0] == 'list':
        content = loadAllSnips()
        pyperclip.copy(content)
        print(content)
    elif para[0] == 'del':
        deleteAllSnips()
        print('Delete all snips')

    else:
        content = loadSnip(para[0])
        pyperclip.copy(content)
        print(content)
else:
    print("""
# mcb.py(w) - Saves and loads pieces of text to the clipboard.
# Usage:
#    mcb.py save <keyword> - Saves clipboard to keyword.
#    mcb.py <keyword> - Loads keyword to clipword.
#    mcb.py list - Loads all keywords to clipboard.   
#    mcb.py del - Delete all keywords from clipboard.
#    mcy.py del <keywordd> - Delete keyword from clipboard. """)
