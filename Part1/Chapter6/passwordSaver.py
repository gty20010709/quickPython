import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] -copy account password')
    sys.exit()
passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

choice = sys.argv[1]

def getPassword(passwords,choice):
    return passwords[choice]

pyperclip.copy(getPassword(passwords,choice))
print('Sucessfully')
