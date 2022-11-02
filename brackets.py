print('........   ........')
print('........   ........')
print('.      .. ..      .')
print('.      .   .      .')
print('.      .. ..      .')
print('.      _____      .')
print('........   ........')
print('........   ........')
print('Use however you like, even commercially, this is free software that can be used by anyone ')
B=['(',')']
bc=0
a='(goofysans(garg))'
G=[]
i=0
while(i<len(a)):
     if(a[i]==B[0]):
          bc=bc+1
     if(a[i]==B[1]):
          bc=bc-1
     if(bc>len(G)):
          G.append('')
     G[bc-1]=G[bc-1]+a[i]
     print(str(bc)+str(G))
     i=i+1
if(bc!=0):
     print('bracket imbalance dectected')
