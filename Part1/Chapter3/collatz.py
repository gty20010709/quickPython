#/bin/python

def collatz(number:int):
    if number % 2 == 1:
        return 3*number + 1
    elif number % 2 == 0:
        return number//2

ipt = eval(input('Please input a number:'))

while True:
    ipt = collatz(ipt)
    print(ipt)
    if ipt == 1:
        break



