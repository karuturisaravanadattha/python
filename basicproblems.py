kg = float(input("Enter weight in kilograms (method 3):"))
pounds = kg*2.20462
print(f"{kg} kilograms is {pounds:.2f} pounds")
-----------------------
  def kg_to_pounds():
    """
    Converts a weight entered in kilograms to pounds.
    """
    try:
        kilograms = float(input("Enter the weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"The weight in pounds is: {pounds:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numerical value for weight.")

# Call the function directly to run the conversion
kg_to_pounds()
  -----------------------------------------
print("number using for loop:")
for num in range(8, 90, 3):
    print(num, end= " ")
-----------------------
print("\nnumber using while loop:")
num =8
while num <= 89:
    print(num,end =" ")
    num +=3
------------------------------
text = input("enter a string :")
chars =list(text)
print("array of characters:",chars)
--------------------------------------
text = input("enter a string:")
chars = []
for ch in text:
    chars.append(ch)
    print("array of characters:",chars)
----------------------------------
# cook your dish here
numbers = [10, 5, 23, 8, 42, 15]
largest_number = max(numbers)
print(f"The largest number in the list is: {largest_number}")
-------------------------------------------
  name = "shanmukh"
age = 20
height = 5.4
print(f"My name is {name}, I am {age} years old, My height is {height} meters")
print(f"shanmukh's father age is {age+25} year old.")
--------------------------------------------
# Take input of heights separated by spaces
heights_input = input("Enter all heights separated by a space: ")

# Convert input into a list of integers
heights = list(map(int, heights_input.split()))

# Count number of people
count = len(heights)
print("Number of people:", count)

# Calculate total height
total = sum(heights)

# Calculate average
avg = total / count
print("Average height:", avg)

# Find heights below average
below_avg = [h for h in heights if h < avg]
print("Heights below average:", below_avg)

