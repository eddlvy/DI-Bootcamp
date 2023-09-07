# EXERCISE 1
my_fav_numbers = {20,22,40,44,4,2,}

my_fav_numbers.add(100)
my_fav_numbers.add(120)

print(my_fav_numbers)

new_my_fav_numbers = list(my_fav_numbers)

new_my_fav_numbers.pop()

my_fav_numbers_2 = set(new_my_fav_numbers)
print(my_fav_numbers_2)

friend_fav_numbers = {43,56,78,11}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

# EXERCISE 2

# no , tuples are inmutable

# EXERCISE 3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# 3.1
basket.remove("Banana")
# 3.2
basket.pop(-1)
# 3.3
basket.append("Kiwi")
# 3.4
basket.insert(1,"Apples")


# 3.5
apple_count = 0

for fruit in basket :
  if fruit == "Apples":
    apple_count += 1
    
print(apple_count)
# 3.6

basket.clear()

# 3.7

print(basket)

# EXERCISE 4

# floats are decimal number, int are whole numbers
# float() function
# 4.3

increment = 1

new_list_decimals = []

for x in range(8):
  increment += 0.5
  new_list_decimals.append(increment)

print(new_list_decimals)

# EXERCISE 5
# 5.1
num = 0

for i in range(20):
  num += 1
  print(num)
print("Out")

# 5.2

list_from_1_to_20 = list(range(1,21))

for number in list_from_1_to_20:
  if list_from_1_to_20.index(number) % 2 == 0:
    print(list_from_1_to_20[number])
print("Out")

# EXECISE 6 

user_name = ""
 
while user_name != "Eduardo" and user_name != "quit" :
  user_name = input("Enter your name\nor write quit to exit\n")
  

print("Your name is equal to my name , or you're a quitter :)")

# EXERCISE 7

# 7.1 # 7.2

user_favorite_fruits = input("Input your favorite fruits separated by a comma\n")

user_favorite_fruits.join(",")
# 7.3
user_order_fruit = input("input any fruit\n")

if user_order_fruit in user_favorite_fruits:
  print("You chose one of your favorite fruits! Enjoy!\n")
else :
  print("You chose a new fruit. I hope you enjoy\n")

  # EXERCISE 8 

# 8.1 8.2 8.3

user_pizza_input = ""
user_pizza_with_toppings = []

while user_pizza_input != "quit" :
    user_pizza_input = input("Enter your Pizza Topings , and type quit to Exit\n")
    user_pizza_with_toppings.append(user_pizza_input)
    print("Topping Added to your pizza")
    if user_pizza_input == "quit":
      user_pizza_with_toppings.pop(-1)
      break
print(f"Your pizza comes with {' and '.join(user_pizza_with_toppings)} and it costs ${10 + (len(user_pizza_with_toppings)*2.5)}" )

# EXERCISE 9
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# 8.2
age_of_customer = (input("Write the age of each family member divided by a comma\n"))

family_members = (age_of_customer.split(","))

total_family_members_age = [int(x) for x in family_members]

total_cost_tickets = 0


# 8.3
for age in total_family_members_age :
  if age > 3 and age <=12:
    total_cost_tickets += 10
  elif age  > 12:
    total_cost_tickets += 15
print(f"Your total price of the tickets for the family is ${total_cost_tickets}")


# EXERCISE 10

# 10.1
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
  sandwich_orders.remove("Pastrami sandwich")
  if "Pastrami sandwich" not in sandwich_orders:
    break
print(sandwich_orders)

# 10.2 10.3

finished_sandwiches = []

for sandwich in sandwich_orders:
  finished_sandwiches.append(sandwich)
  print(f"i made your {sandwich}")






  
  
  


  



  



  
  












  













 
 

  
    
    
    
    





    










  








  # EXERCISE 6


  
  


  



















