from pickletools import string1
import re

def regexStrip(string:str,splitchar:str=' '):
    if splitchar == ' ':
        result = re.findall(r'\s*(.*)\s*',string)
        result = ''.join(result)
        return result
    else:
        regex = re.compile(r'{}'.format(splitchar))
        result = regex.sub('',string)
        return result

print(regexStrip('apple,bnana,cup,desk','apple'))

str.strip()

