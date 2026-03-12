
---LOOPS AND TUPLES----------
numbers= [2,3,4,5,6]
squares =[]
for i in numbers:
    square = i**2
    squares.append(square)
    print("the list of squares is :",squares)




tuple1 = (2,56,34,3,5,-1)
for i in tuple1:
    print(i)
    if i==5:
        break
else:
    print("loop is sucessfully excuted")


tuple1 = (2,56,34,3,5,-1)
for i in tuple1:
    print(i)
    if i%4 == 0:
        break
else:
    print("there is no value that is in the tuple")

