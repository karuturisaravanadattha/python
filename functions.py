import math 

def paint_calculation(height,width,cover):
    area = height * width
    no_of_cans = math.ceil(area/cover)
    print(f"you will need {no_of_cans} cnas of paint.")


h =int(input("enter the height of wall in meter:\n"))
w = int(input("enter the width of wall in meter:\n"))
coverage =7
paint_calculation(width=w,height=h,cover=coverage)



def add(*numbers):
    c=0
    for i in numbers:
        c += i
    print(f"sum  is {c}")

add(1,2)
add(3,4,5)
add(6,7,8,9,0)



def info_person(*args, **kwargs):
    for key, value in kwargs.items():   # use .items(), not .item()
        print(key, value)
    print(args)

# Test cases
info_person(1, 2, name="ram", age="20", dept="cse")
info_person(1, 2, 3, name="kavya", dept="ece")




def greet(name,dept):
    print(f"hi {name}")
    print(f"are you from {dept} department")

greet("jenny","cs")



import math
def prime_checker(number):
    is_prime = True
    if number == 1:
        is_prime=False
    for i in range(2,math.ceil(number/2)+1):
        if number%i == 0:
            is_prime == False
    if is_prime:
        print("it is a prime number")
    else:
        print("not a prime number")
n=int(input("enter the number"))
prime_checker(n) 



# Prompt user for input
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display results
print("Weight:", weight)
print("BMI:", int(bmi))  # Displaying BMI as an integer
--------------------------------------
  def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(1, 10):
    print(fib(i),end=" ")
--------------------------------------------
def fibonacci_memoization(n, memo={}):
    """
    Calculates the nth Fibonacci number using recursion with memoization
    (dynamic programming).
    """
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
        return memo[n]
