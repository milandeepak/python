# Write a program which takes an integer array and the number of elements in that array as input
#  and display the mode of numbers in the array and number of occurrences of the mode.

#The mode of a list of numbers is the number that occurs most frequently in the list. 
# e.g. The mode of 5, 6, 7, 7, 6, 6, 6, 4, 3 is 6 since it occurs 4 times.
def mode(list,n):
 c=0
 num = 0
    
 for i in list:
   if i>num:
    num=i
    c=1    
   elif i==num:
     c = c + 1
 return c

n=9
list = [1,3,6,5,4,8,6]   
c = mode(list,n)
print(c)         





