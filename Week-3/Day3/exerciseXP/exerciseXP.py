# EXERCISE 1




class Currency:
  def __init__(self, currency, amount):
    self.currency = currency
    self.amount = amount

  def __str__(self):
    return f"{self.currency} , {self.amount}s"
  
  def __int__(self):
    return f"{int(self.amount)}"
  
  def __repr__(self):
    return f"{self.amount} {self.currency}s"

  def __add__(self,x):
    try: 
      if self.currency != x.currency:
        print("Type error")
      return self.amount + x.amount
    except: 
      return self.amount + x
      
    
    
  def __iadd__(self,x):
    try:
      if self.currency != x.currency:
        print("Type error")
    except:
      if self.currency == x.currency:
        return self.amount + x.amount 


    
  
            
            
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)  

print(c1 + 3)

# EXERCISE 3

from random import randint ,choice

def random_num(x):
    if 1 < x < 100:
      ran_num = randint(1,100)
      if x == ran_num:
         print("Success")
      else:
         print("Try again")

random_num(5)

# EXERCISE 4

import string


def rand_str(chars = string.ascii_uppercase + string.ascii_lowercase):
	return ''.join(choice(chars) for _ in range(5))


print(rand_str())

# EXERCISE 5

import datetime

def current_date():
    date = datetime.datetime.now()
    print(date)

current_date()

# EXERCISE 6

def time_until_january():
   today = datetime.datetime.now()
   future_date = datetime.datetime(2024, 1, 1)
   time_to_january = future_date - today
   print(f"The time until january is {time_to_january}")

time_until_january()

# EXERCISE 7
# from math import ceil

def time_of_your_life_in_minutes(year,month,day):
   today = datetime.datetime.now()
   birthday = datetime.datetime(year, month, day)
   total_time = today - birthday
   minutes = total_time.total_seconds()//60
   
   print(f"You have lifed {minutes} minutes")

time_of_your_life_in_minutes(1985,8,22)

# EXERCISE 8

from faker import Faker
fake = Faker()

users = [{}] 


users[0]["name"] = fake.name()
users[0]["address"] = fake.address()
users[0]["language_code"] = fake.language_code()

print(users)












  
  
  
  


       
     


    





# EXERCISE 4  


      
    
    
    















