
# EXERCISE 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

keys_and_values_list = zip(keys,values)

new_dict = dict(keys_and_values_list)
print(new_dict)


# EXERCISE 2 Cinemax

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name,age in family.items():
  if age > 12 :
    total_cost+=15
  elif age <=12 and age >3 :
    total_cost+=10
print(f"the cost for all the family is {total_cost}")

# EXERCISE 3 Zara

brand = {
  'name': "Zara" ,
  'creation_date': 1975 ,
  'creator_name': "Amancio Ortega Gaona" ,
  'type_of_clothes': ["men", "women", "children", "home"], 
  'international_competitors' :[ "Gap", "H&M", "Benetton" ],
  'number_stores': 7000 ,
  'major_color' : {
    'France': "blue", 
    'Spain': "red", 
    'US': ["pink", "green"]}
}

brand["number_stores"] = 2
print(f"{brand['name']} clients are {brand['type_of_clothes']}")
brand['country_creation'] = "Spain"
print(brand)

for key in brand :
  if key == 'international_competitors':
    brand[key].append("Desigual") 
print(brand)

brand.pop('creation_date')
print(brand)

print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand.keys()))
print(brand.keys())

more_on_zara = {
  'creation_date': 1975 ,
  'number_stores': 10000
}

brand.update(more_on_zara)
print(brand['number_stores'])#Change to 10000

# EXERCISE 4


    
 #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# 4.1
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {}

count = -1

for value in users:
  count += 1
  disney_users_A.update({value : count})
print(disney_users_A)
  
# 4.2

new_users_list = list(enumerate(users))
disney_users_B = dict(new_users_list)
print(disney_users_B)

# 4.3
new_sorted_keys=  list(sorted(disney_users_A.keys()))

disney_users_C = {}

count_2 = -1

for i in new_sorted_keys:
  count_2 += 1
  disney_users_C.update({i : count_2})
print(disney_users_C)

# 4.4
# 4.4.1

disney_users_no_i = {}
count_i = -1

for key in disney_users_A:
  if "i" in key:
    count_i += 1
    disney_users_no_i.update({key : count_i})
  else:
    continue
print(disney_users_no_i)



    
    
  
  

























  




