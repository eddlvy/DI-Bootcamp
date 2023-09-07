# exercises

# my_age = 38

# years = 123879

# my_future_age = years + my_age

# print(my_future_age)

# first_name = "Eduardo"

# last_name = "Levy"

# full_name = f"My full name is {first_name} {last_name}"

# print(full_name)

# # shift + 3 to comment in the middle of a line

# # 1

# user_miles = float(input("input miles "))

# miles_converter = user_miles*1.61

# print(miles_converter)

# 2

# name = 'John Doe'
# if len(name) > 20:
#     print(f"Name "{name}" is more than 20 chars long")
#     length_description = 'long'
# elif len(name) >15:
#      print(f"Name "{name}" is more than 15 chars long")
#     length_description = 'semi long'
# elif len(name) > 10:
#      print(f"Name "{name}" is more than 10 chars long")
#     length_description = 'semi long'
# elif len(name) == 8 and len(name) or 9 and len(name) ==10 and len(name) == 20:
#      print(f"Name "{name}" is 8, 9 or 10 20 chars long")
#     length_description = 'semi short'
# else:
#      print(f"Name "{name}" is a short name")
#     length_description = 'short'

# 3

# # of guests	price
# Up to 50 people	$4,000
# Up to 100 people	$10,000
# Up to 200 people	$15,000
# More than 200 people	$20,000

guests_number = int(input("How many people be attending"))

print(guests_number)

if guests_number <= 50:
    print("The wedding will cost $4000 ")
elif guests_number <= 100:
    print("The wedding will cost $10000 ")
elif guests_number <= 200:
    print("The wedding will cost $15000 ")
else:

    print("The wedding will cost $20000 ")
