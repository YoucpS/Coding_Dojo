lowNum=500
highNum=80
mult=49

while lowNum%mult!=0:
    lowNum=lowNum*mult
else:
    print(lowNum)

while highNum%mult!=0:
    highNum=highNum*mult
else:
    print(highNum)

print(mult)