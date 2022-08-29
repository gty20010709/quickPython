
def listJ(ls:list):
    joinPart = ls[:-2]
    string = ", ".join(joinPart)
    string = string + ", and {}".format(ls[0])
    return string
spam = [str(i) for i in range(5)]

result = listJ(spam)
print(result)
