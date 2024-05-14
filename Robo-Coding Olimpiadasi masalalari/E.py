a,b,c=input(),input(),input()
e,r,t=0,0,0
for k,i in {'a':a,'b':b,'c':c}.items():
  for k1,j in {'a':a,'b':b,'c':c}.items():
    if (i=='qog\'oz' and j=='quduq') or (i=='quduq' and j=='qaychi') or (i=='qaychi' and j=='qog\'oz'):
      if k=='a':e+=1
      if k=='b':r+=1
      if k=='c':t+=1
print('Ali' if e>0 and 1>r and 1>t else 'Vali' if  r>0 and 1>e and t<1 else 'G\'ani' if t>0 and 1>r and 1>e else '?')