chapter11.q1
lst = [0,1]
a = 0
b = 1
c = 0
for i in range(7):
    c = a + b
    a = b
    b = c
    lst.append(c)

tup = tuple(lst)
print("9 terms of Fibonacci series are:", tup)
  

chapter11.q2(a)
tup = eval(input("Enter the elements of tuple:"))
b = int(eval(input("Enter the index value:")))
c = len(tup)
if b < c:
    print("value of tuple at index", b ,"is:" ,tup[b])
else:
    print("Index is out of range")


chapter11.q2(b)
term = int(input ("Enter Fibonacci Term: "))
fib = (0,1)
while(fib[len(fib) - 1] < term):
    fib_len = len(fib)
    fib = fib + (fib[fib_len - 2] + fib[fib_len - 1],)

fib_len = len(fib)

if term == 0:
    print("0 is fibonacci term number 1")
elif term == 1:
    print("1 is fibonacci term number 2")
elif fib[fib_len - 1] == term:
    print(term, "is fibonacci term number", fib_len)
else:
    print("The term", term , "does not exist in fibonacci series")



chapter11.q3
n = eval(input("Enter the numbers: "))
tup = tuple(n)
print("Tuple is:", tup)
print("Highest value in the tuple is:", max(tup))
print("Lowest value in the tuple is:", min(tup))



chapter11.q4
tup = ()
ans = "y"
while ans == "y" or ans == "Y" :
      roll_num = int(input("Enter roll number of student: "))
      name = input("Enter name of student: ")
      marks = int(input("Enter marks of student: "))
      tup += ((roll_num, name, marks),)
      ans = input("Do you want to enter more marks? (y/n): ")
print(tup)



chapter11.q5
num_of_students = 5
tup = ()
for i in range(num_of_students):
    print("Enter the marks of student", i + 1)
    m1 = int(input("Enter marks in first subject: "))
    m2 = int(input("Enter marks in second subject: "))
    m3 = int(input("Enter marks in third subject: "))
    tup = tup + ((m1, m2, m3),)
    print()
    
print("Nested tuple of student data is:", tup)



chapter11.q6
num_of_students = 5
tup = ()
for i in range(num_of_students):
    print("Enter the marks of student", i + 1)
    m1 = int(input("Enter marks in first subject: "))
    m2 = int(input("Enter marks in second subject: "))
    m3 = int(input("Enter marks in third subject: "))
    tup = tup + ((m1, m2, m3),)

for a in range(num_of_students):
    sum = (m1+m2+m3)
    avg = (sum)/3
    print(f"The sum of student{a+1}: ", sum)
    print(f"The average of student{a+1}: ", avg)
  

chapter11.q7
tup1 = eval(input("Enter the elements of first tuple: "))
tup2 = eval(input("Enter the elements of second tuple: "))
tup3 = tup1 + tup2
print(tup3)


chapter11.q8
str_tuple = ("computer science with python" ,"Hello Python" ,"Hello World" ,"Tuples")
shortest_str = min(str_tuple)
shortest_str_len = len(shortest_str)
print("The length of shortest string in the tuple is:", shortest_str_len)


chapter11.q9(a)
tup = ()
for i in range(1,51):
    tup = tup + (i**2,)
print("The square of integers from 1 to 50 is:" ,tup)

chapter11.q9(b)
tup = ()
for i in range(1, 27):
    tup = tup + (chr(i + 96)* i,)
print(tup)


chapter11.q10
tup = ((2,5),(4,2),(9,8),(12,10))
count = 0
tup_length = len(tup)
for  i in range (tup_length):
    if tup [i][0] % 2 == 0 and tup[i][1] % 2 == 0:
        count = count + 1
print("The number of pair where both a and b are even:", count)

chapter11.q11
seq_a = eval(input("Enter the first tuple: "))
seq_b = eval(input("Enter the second tuple: "))

for i in seq_a:
    if i not in seq_b:
        print("False")
        break
else:
    print("True")



chapter11.q12
tup = eval(input ("Enter the numeric tuple: "))
total = sum(tup)
tup_length = len(tup)
mean = total / tup_length
print("Mean of tuple:", mean)



chater11.q13
tup = eval(input("Enter a tuple: "))
maxCount = 0
mode = 0

for i in tup :
      count = tup.count(i)
      if maxCount <  count:
            maxCount = count
            mode = i
print("mode:", mode)




chapter11.q14
import statistics 

tup = eval(input("Enter a tuple: "))
tup_sum = sum(tup)
tup_len = len(tup)

print("Average of tuple element is:", tup_sum / tup_len)
print("Mean of tuple element is:", statistics.mean(tup))



chapter11.q15
tup1 = ((1, 2), (3, 4.15, 5.15), ( 7, 8, 12, 15))
total_mean = 0
tup1_len = len(tup1)

for i in range(tup1_len):
    mean = sum(tup1[i]) / len(tup1[i])
    print("Mean element", i + 1, ":", mean)
    total_mean = total_mean + mean

print("Mean of means" ,total_mean / tup1_len)
