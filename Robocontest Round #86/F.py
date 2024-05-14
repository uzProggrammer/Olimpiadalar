a,b=map(int,input().split())
d=[]
for i in range(a,b+1):
    if bin(i)[2:].count('1')==bin(i)[2:].count('0'):
        d.append(i)

print(d)
print(len(d))