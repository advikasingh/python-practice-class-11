#chapter6-q2.py
date = int(input("enter today's date:"))
NOD = 30-date;
print("no.of days left are ", NOD)


#chapter6-q3.py
a = 5
b = a*2
c = b-1
print(a)
print(b)
print(c)

#chapter6-q5.py
a = int(input("enter a number:"))
p,q,r,s,t = a*1, a*2, a*3, a*4, a*5
print(p,q,r,s,t)

#chapter6-q6.py
radius = int(input("enter radius:"))
area = 22*radius*radius/7
print(area)

#chapter6-q7.py
a = int(input("enter english marks"))
b = int(input("enter maths marks"))
c = int(input("enter cs marks"))
d = int(input("enter chemistry marks"))
f = int(input("enter physics marks"))
am = (a+b+c+d+f)/5
print("your average marks are:", am)

#chapter6-q8.py
height = int(input("enter your height in cm:"))
inch = height/2.54
feet = inch/12
print("your height in inches:", inch)
print("your height in feet:", feet)

#chapter6-q9.py
q = int(input("enter a number"))
a = q*q
b = q*q*q
c = q*q*q*q
print(a,b,c)

#chapter6-q10.py
base = int(input("enter base:"))
height = int(input("enter height:"))
area = (1*base*height)/2
print(area)

#chapter6-q11.py
p = int(input("enter principle amount"))
r = int(input("enter rate"))
t = int(input("enter time period"))
n = int(input("enter the number of times rate is compounded"))
s = p*r*t/100
c = p(1+r/n)**(n*t)
print("the simple interest is:", s)
print("the compound interest is:", c)

#chapter6-q12.py
n = int(input("enter number:"))
a = n*1
b = n*2
c = n*3
d = n*4
f = n*5
print("the first five multiples are:", a,b,c,d,f)

#chapter6-q13.py
name = input("name:")
c = int(input("class:"))
a = int(input("age:"))
print(name,c,a)
print(name)
print(c)
print(a)

#chapter6-q14.py
n = int(input("enter a number between 1-7:"))
a = 100*n+10*(n+1)+(n+2)
print("the 3 digit number is:", a)

#chapter6-q15.py
a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
c = int(input("enter 3rd number:"))
print("the original numbers are:", a,b,c)
a = a+b
b = b+c
print("the swapped numbers are:", a,b,c)
