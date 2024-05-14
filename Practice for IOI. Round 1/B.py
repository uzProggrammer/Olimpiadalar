a,b=map(int,input().split())
d,d2=[],[]
for i in range(b):
  e,d1=map(int,input().split())
  d2.append(d1)
q=int(input())
s=[]
max=0
for i in range(q):
  t,y=input().split()
  if t=='+':s.append(y)
  else:s.remove(y)
  if len(s)==1:print(0);max=0
  elif len(s)==0:print(-1);max=0
  else:
    if max<d2.index(int(y))+1:
        max=d2.index(int(y))+1
        print(d2.index(int(y))+1)
    else:print(max)