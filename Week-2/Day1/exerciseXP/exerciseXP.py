# exercise 1
print(("Hello World ")*4)


# exercise 2
print((99**3)*8)
# exercise 3
# false
# true
# false
# false
# true

# exercise 4

computer_brand = "Dell"

print(f"I have a {computer_brand} computer")

# exercise 5

name = "Eduardo"
age = 38
shoe_size = 45
info = f"My name is {name} , i'm {age} years old and i wear a {shoe_size} shoe"

print(info)

# exercise 6

a = 40
b = 22
if a > b:
    print("Hello World")


# exercise 7

user_number = int(input("Please write a number \n "))

if (user_number % 2) == 0:
    print(f"{user_number} is even")

else:
    print(f"{user_number} is odd")

    # exercise 8
user_name = input("Write your name \n")

if user_name == name:
    print("Hey ,we have the same name :)")

else:
    print("Sorry, your name is not as cool as mine ;)")

 # exercise 9

user_heigth = float(input("please write your heigth in inches \n"))

inches_to_cm = user_heigth*30.48

if inches_to_cm > 145:
    print("You're tall enough to ride the roller coaster")
else:
    print("you need some extra inches to ride the coaster :)")
