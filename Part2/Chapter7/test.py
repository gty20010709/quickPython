import re

Regex = re.compile('(H)a+')
text = '''
Ha
Haa
Haaa'''

mo = Regex.finditer(text)
# print(mo)
for i in mo:
    print(i.group())


# emailRegex = re.compile(r'(\d+|\w+|[+%])+\@\w+\.\w+')
# text = '''
# 18009657192
# afajdga
# abc@gal.com
# abc_def@foxmail.com
# 123456789@qq.com
# ajfla
# abc+d@qq.com
# def%fak@com.com
# flkajdgk
# '''

# mo = emailRegex.findall(text)

# for x in mo:
#     print(x.groups)