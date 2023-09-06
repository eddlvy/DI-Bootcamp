# EXERCISE 1

def display_message():
  print("Im learning Full Stack Development")
display_message()

# EXERCISE 2

def favorite_book(title):
  print(f"One of my favorite books is {title}")

favorite_book("Sinuhe the Egiptian")

# EXERCISE 3

def describe_city(city,country = "Cuba"):
  print(F"{city} is in {country}")

describe_city("Havana")

# EXERCISE 4

def random_num():
  import random
  num_ran = random.randint(0,100)
  return num_ran

random_num()

ran_num = random_num()


def get_random_number (x):
  if x > 100:
    return print("Number over 100,not good")
  if 100 > x > 1 and x == ran_num:
    print(f"It's the same number!")
  else :
    print(f"Noooo , {x} and {ran_num} are not the same")

get_random_number(3)
get_random_number(101)

# EXERCISE 5

def make_shirt(size = "L",message = "I LOVE PYTHON"):
  print(f"The size of the shirt is {size} and the text is {message}")

make_shirt()
make_shirt("M")
make_shirt("S","I'M BORED")

# EXERCISE 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
  for name in magician_names:
    print(name)
    

show_magicians()

def make_great():
  for i in range(len(magician_names)):
    if i <= 2:
      magician_names[i] = "The Great " + magician_names[i]
    else:
     return magician_names

make_great()

# print(magician_names)

show_magicians()

# EXERCISE 7

# 7.1


# def get_random_temp():
#    import random
#    ran_temp = random.randint(-10,40)
#    return ran_temp

# get_random_temp()
# print(get_random_temp())

# 7.2 7.3

# def main():
#   temp = get_random_temp()
#   print(f"The temperature now is {temp} degrees celsius")
#   if temp < 0 :
#     print("Brrrrr, that's freezing! Wear some extra layers today")
#   elif 16 > temp > 0:
#     print("Quite chilly! Don't forget your coat")
#   else :
#     print("Go outside and have fun")

# main()

# 7.4.1.2.3.4

def get_random_temp(season):
   if season == "winter":
     import random
     ran_temp = random.randint(-10,0)
     return ran_temp
   if season == "spring":
     import random
     ran_temp = random.randint(11,20)
     return ran_temp
   if season == "summer":
     import random
     ran_temp = random.randint(21,40)
     return ran_temp
   if season == "autumn":
     import random
     ran_temp = random.randint(1,10)
     return ran_temp
   
def main():
  user_input_season = input("Write the season\n")
  temp = get_random_temp(user_input_season)
  print(f"The temperature now is {temp} degrees celsius")
  if temp < 0 :
    return    print("Brrrrr, that's freezing! Wear some extra layers today")
  if 16 > temp > 0:
    return  print("Quite chilly! Don't forget your coat")
  if 40 > temp > 16:
    return print("Go outside and have fun")
  
main()






    

  
    


  







 



  
  




# EXERCISE 7











  
    
    
  


    





 










    




 
    


  
