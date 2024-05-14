l=int(input())
d=[]
for i in range(2,l):
  for j in range(2,l):
    if i!=j and i*j==l:
      d.append([str(i),str(j),])
print(len(d))
for i in d:
  print(*i)