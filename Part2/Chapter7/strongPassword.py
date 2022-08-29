import re

def pdChecker(password):
    if len(password) < 8:
        return False
    if len(re.findall(r'[a-z]',password)) == 0:
        return False
    if len(re.findall(r'[A-Z]',password)) == 0:
        return False
    if len(re.findall(r'[0-9]',password)) == 0:
        return False
    return True

while True:
    password = input('Input password')
    print(pdChecker(password))

