i= int(input("Enter number:"))
rev=0
while i!=0:
    n = i%10
    rev=rev*10+n
    i=i/10
print(rev)

