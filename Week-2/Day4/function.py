# 1. create a function that takes a number as an argument, and check if this number is even or odd
# 2. create a function that takes a list of numbers as an argument, and check if each number is even or odd


# exercises

# def chech_number(x):
#   if x % 2== 0:
#     print(f"{x} It's even")
#   else :
#     print(f"{x} It's odd")

# chech_number(3)



# def list_number(values):
#   for y in values:
#     if y % 2 == 0:
#       print(f"{y} It's even")
#     else :
#       print(f"{y} It's odd")

# list_number([1,2,3,4,5])

# more exercises


def get_price_car():
  age = int(input("input your age\n"))
  if age >= 40:
      return 200
  if age < 40 :
      return 300
  

def get_price_fligth():
  user_destination = input("input your destination\n")
  if user_destination == "Paris":
    return 400
  else :
    return 600
  
def inform_user_vacation():
   total = get_price_car() + get_price_fligth()
   print(f"Your total is ${total}")

inform_user_vacation()
  








  

 




  
  





