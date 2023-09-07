# list comprehension


# list1 = [1,2,3,4]
# number_list = [ x+1 for x in len(list1)]

# dictionaries

prices = {
  'apple' : 2,
  'banana' : 5,
  'orange' :1
}

user_input = input("what fruit you want\n")

price_of_the_fruit = prices[user_input]

print(price_of_the_fruit)

# exercise

# create a new list that only contains the uppercased words
words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']


new_list = []
new_list = [word for word in words if word.isupper() ]
print(new_list)

