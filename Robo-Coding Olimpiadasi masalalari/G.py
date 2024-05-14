a=input()
d={}
for i in range(len(a)-1):
  for j in range(len(a)-1):
    if i!=j and a[i:j] not in d:
      c=1;k=0
      while k!=len(a):
        try:
          e=''.join([l for l in range(len(a)-1) if l!=i])
        except:
          e=a[:k:][:i+1:]
        print(e)
        if a[i:j] in e:c+=1
        k+=1
      d[a[i:j]]=c
print(d)