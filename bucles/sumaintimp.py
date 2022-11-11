x = 0

for x in range(0,500001):
    if x%2==0:
        x=x+1
    else:
        y=x
        j=y+x
        x=x+1
print(j)
