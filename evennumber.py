#A Program to find whether the given input is even or odd.!
import random
evenlist=[]
oddlist=[]
while 1:
    number=int(input("enter the input value:"))
    x=number%2
    if x==0:
        print("the number is even")
        evenlist.append(number)
        print("the numbers in even List are:")
        print(evenlist)
        
     
    else:
        print("the number is odd")
        oddlist.append(number)
        print("the numbers in odd List are:")
        print(oddlist)
        
