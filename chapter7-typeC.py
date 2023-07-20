#chapter7-q2.py
a = int(input("enter temperature on monday"))
b = int(input("enter temperature on tuesday"))
c = int(input("enter temperature on wednesday"))
d = int(input("enter temperature on thursday"))
e = int(input("enter temperature on friday"))
f = int(input("enter temperature on saturday"))
g = int(input("enter temperature on sunday"))

avgt = (a+b+c+d+e+f+g)/7
print("the average temperature of the week is", avgt)

#chapter7-q3.py
x = int(input("enter 1st number"))
y = int(input("enter 2nd number"))
z = int(input("enetr 3rd number"))

a = 4*x**4+3*y**3+9*z+6*3.14
print("the answer is", a)

#chapter7-q4.py
seconds = int(input("Enter the number of seconds: "))

minutes = seconds // 60
remaining_seconds = seconds % 60

print(f"{seconds} seconds is equal to {minutes} minutes and {remaining_seconds} seconds.")

#chapter7-q5.py
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")year = int(input("Enter a year: "))

#chapter7-q6.py
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % num2 == 0:
    print(f"{num1} is fully divisible by {num2}.")
else:
    print(f"{num1} is not fully divisible by {num2}.")

#chapter7-q7.py
x = int(input("Enter a two digit number: "))
y = x % 10 * 10 + x // 10
print("Reversed Number:", y)

#chapter7-q8.py
x = int(input("Enter a two digit number: "))
d1 = x % 10
x //= 10
d2 = x % 10
x //= 10
d3 = x % 10
y = d1 * 100 + d2 * 10 + d3
print("Reversed Number:", y)

#chapter7-q9.py
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day: "))

if month < 1 or month > 12 or day < 1 or day > 30:
    print("Invalid input. Please enter valid month (1-12) and day (1-30).")
else:
    day_of_year = (month - 1) * 30 + day
    print(f"The given date is day {day_of_year} of the year.")

#chapter7-q10.py
age = int(input("Enter your age: "))
age_after_10_years = age + 10
print(f"In 10 years, You will be {age_after_10_years} years old!")

#chapter7-q11.py
y = float(input("How many years? "))

d = y * 365
h = d * 24
m = h * 60
s = m * 60

print(y, "years is:")
print(d, "days")
print(h, "hours")
print(m, "minutes")
print(s, "seconds")

#chapter7-q12.py
#samplerun1
a = int(input(" Random number between 0 and 5 (A): "))
b = int(input(" Random number between 0 and 5 (B): "))
c = a**b
print("A to the power B = ", c)

#samplerun2
a = int(input(" Random number between 0 and 5 (A): "))
b = int(input(" Random number between 0 and 5 (B): "))
c = a**b
print("A to the power B = ", c)

#samplerun3
a = int(input(" Random number between 0 and 5 (A): "))
b = int(input(" Random number between 0 and 5 (B): "))
c = a**b
print("A to the power B = ", c)

#chapter7-q13.py
import random
import statistics

start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
step = int(input("Enter step: "))

a = random.randrange(start, stop, step)
b = random.randrange(start, stop, step)
c = random.randrange(start, stop, step)
d = random.randrange(start, stop, step)
e = random.randrange(start, stop, step)
f = random.randrange(start, stop, step)

print("Generated Numbers:")
print(a, b, c, d, e, f)

seq = (a, b, c, d, e, f)

mean = statistics.mean(seq)
median = statistics.median(seq)
mode = statistics.mode(seq)

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)

#chapter7-q14.py
import random

def generate_random_divisible_by_5():
    random_numbers = []
    while len(random_numbers) < 3:
        num = random.randint(100, 199)
        if num % 5 == 0:
            random_numbers.append(num)
    return random_numbers

try:
    random_numbers = generate_random_divisible_by_5()
    print("Generated random numbers divisible by 5:", random_numbers)

except Exception as e:
    print(f"Error: {e}")
    
#chapter7-q15.py
import secrets

def generate_otp():
    return secrets.randbelow(900000) + 100000

try:
    random_otp = generate_otp()
    print("Generated OTP:", random_otp)
    
except Exception as e:
    print(f"Error: {e}")

#chapter7-q18.py
a = int(input("enter area of sphere: "))
r = math.sqrt(a/4*3.14)
print("the radius of the sphere is: ", r)
