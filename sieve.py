s=['80mm','40mm','20mm','10mm','4.75mm','2.36mm','1.18mm','600μm','300μm','150μm','Pan']
w_s=[]
for i in s:
  a=int(input('Enter the retained weight in '+i+' sieve:'))
  w_s.append(a)
pw_s=[]
for i in w_s:
 pw_s.append(i/10)
print(pw_s)





