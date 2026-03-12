numbers = input("enter the list of number: ")  # user enters numbers as a string
numbers_list = numbers.split()  # split string into list of strings
count = 0

# count elements manually
for i in numbers_list:
    count = count + 1
print(f"the length of the list : {count}")

# convert elements to integers
for i in range(count):
    numbers_list[i] = int(numbers_list[i])

# initialize maximum
maximum_number = numbers_list[0]

# find max manually
for number in numbers_list:
    if number > maximum_number:
        maximum_number = number
print(f"the maximum number is : {maximum_number}")




for number in range(1,100):
    if number%3==0 and number%5==0:
        print("fiZZbuzz")
    elif number%3==0:
        print("fizz")
    elif number %5==0:
        print("buzz")
    else:
        print(number)

