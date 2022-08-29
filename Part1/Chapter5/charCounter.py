import pprint

message = 'This is a message to test the func of Character counter.'

d = {}

for i in message:
    d.setdefault(i,0)
    d[i] = d[i] + 1

pprint.pprint(d)
