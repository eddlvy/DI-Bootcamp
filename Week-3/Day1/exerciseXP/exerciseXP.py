# 
# EXERCISE 1

class Cat():
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Blacky",2)
cat2 = Cat("Lucky",4)
cat3 = Cat("Whiskers",7)


# print(list_cats[0].age)
# print(list_cats[0].name)


def oldest_cat():
    list_cats = [cat1,cat2,cat3]
    # cat_age = list_cats[0].age
    oldest_cat = list_cats[0]
    # cat_age = list_cats[0].age
    for cat in list_cats:
       if  oldest_cat.age < cat.age:
           oldest_cat = cat
        
       
    return oldest_cat

       
        
    
       

cat_name = oldest_cat()

print(cat_name.name)
        
       


       
# print(f"The oldest cat is {cat_name.name} and is {cat_name.age}")
       

    

# EXERCISE 2




class Dog():

  def __init__(self,name,heigth):
      self.name = name
      self.heigth = heigth

  def bark(self):
      return f"{self.name} goes Woof" #Do not print here, just return an f string

  def jump(self,x):
      x = self.heigth*2
      return f"{self.name} jumps {x} cm high" #return an f string

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)








print(f"{davids_dog.name} heigth is {davids_dog.heigth} and {davids_dog.bark()} and jumps {davids_dog.jump(40)}") #cannot print twice

print(f"{sarahs_dog.name} heigth is {sarahs_dog.heigth} and {sarahs_dog.bark()} and jumps {sarahs_dog.jump(40)}")

def bigger_dog():
  dog_list = [davids_dog,sarahs_dog]
  bigger = dog_list[0]
  for dog in dog_list:
    if bigger.heigth < dog.heigth:
       bigger = dog
  return bigger
bigger_dog_name = bigger_dog()
print(f"the bigger dog is {bigger_dog_name.name}")

# EXERCISE 3

class Song():
   def __init__(self,lyrics):
      self.lyrics = list(lyrics)
      
      
   def sing_me_a_song(self):
      for item in self.lyrics:
         print(item)

stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()

# EXERCISE 4

class Zoo():
   def __init__(self,zoo_name):
      self.animals = []
      self.name = zoo_name

   def add_animal(self,new_animal):
      if self.animals != new_animal:
         self.animals.append(new_animal)
      return self.animals
   def get_animal(self):
      return f"{self.animals}"
   def sell_animal(self,animal_sold):
      if animal_sold in self.animals:
         self.animals.remove(animal_sold)
      return self.animals
   def sort_animals(self): #4.6
       sorted_animal_list = sorted(self.animals)
       first_char = "a"
       for char in enumerate(sorted_animal_list):
          if char[0] == first_char:
            #  stuck here how to group into a dict 
             
             
             
              
           



      
   

         
         
      

      
  











       
    








      
    






    
  