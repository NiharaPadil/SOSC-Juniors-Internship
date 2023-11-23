import random
import itertools

print("Welcome to the Password generator")


x=int(input("How many letters you want in your password: "))
a="abcdefghijABCDEFGHIklmnopqvwxyzJKLMNOPrstuQRSTUVWXYZ"
alp=random.sample(a,x)

y= int(input("How many numbers you want in your password: "))
b=[i for i in range (10)]
num=random.sample(b,y)

z= int(input("How many symbols you want in your password: "))
c ="!@#$%^&*\<>/?~"
symb=random.sample(c,z)

print("This is your password as per your requirements: ")
var=list(itertools.chain(alp,num,symb))
final=random.sample(var,len(var))
for i in range(len(final)):
    print(final[i],end="")