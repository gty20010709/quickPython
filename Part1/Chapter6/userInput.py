def inputAge():
    while True:
        ipt = input('Please input your age:')
        if ipt.isdecimal():
                break
        print('Please input again, such as 42')
    return ipt

def inputPassword():
    while True:
        ipt = input('Please input your password:')
        if ipt.isalnum():
            break
        print('Please input password ( only num and alpha)')
    return ipt

print(inputAge())
print(inputPassword())

