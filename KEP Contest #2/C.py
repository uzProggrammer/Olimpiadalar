a=int(input())
i=a+1

while True:
  if str((i**2+a**2)**0.5).split('.')[1]=='0':
    print(a,i)
    exit()
  i+=1
print(-1)