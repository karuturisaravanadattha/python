import random 
#-------------------------------
#a = random.randint(1,7)
#a = random.randrange(1,3)
#a = random.random()
#a = random.uniform(1,3)
#l=[1,2,3,4,465,778,98]
#a = random.choice(l)
#random.shuffle(l)
#print(l)


#-------------------------

side=random.randint(0,1)
print(side)
if side == 1:
    print("HEADs")
else:
    print("TAILs")

#-------------------------------------

names_list= input("enter the names by separated by comma:")
names_list = names_list.split(",")
#print(names_list)
length = len(names_list)
random_choice=random.randint(0,length-1)
print(f"{names_list[random_choice]} will pay the bill")
  --------------------------------------------------
import random
user_choice=int(input("enter your choice: type 0 for rock, 1 for paper,2 for scissors."))
if user_choice >=3 or user_choice < 0:
    print("you entered invalid  number, you lose.")
else:
    computer_choice = random.randint(0,2)
    print("computer choice")
    print(computer_choice)
    if computer_choice == user_choice:
        print("IT's DRAW")
    elif computer_choice == 0 and user_choice == 2:
        print("YOU LOSE")
    elif computer_choice == 2 and user_choice == 0:
        print("YOU WIN")
    elif computer_choice > user_choice:
        print("YOu lose")
    elif computer_choice < user_choice:
        print("you Win")
