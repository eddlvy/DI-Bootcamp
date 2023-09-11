# EXERCISE 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    pass

all_cats = [Bengal("Lucky",2),Chartreux("Whiskers",12),Siamese("Dracula",3)]
sara_pets = Pets(all_cats)

sara_pets.walk()

# EXERCISE 2

class Dog():
    def __init__(self,name,age,weigth):
        self.name = name
        self.age = age 
        self.weigth = weigth

    def bark(self):
        return f"{self.name} is barking Wouf Wouf"
    
    def run_speed(self):
        return self.weigth/self.age*10
    
    def figth(self,other_dog):
        if self.run_speed() > other_dog.run_speed():
            return f"{self.name} is the winner of the figth***"
        elif self.run_speed() < other_dog.run_speed():
            return f"{other_dog.name} is the winner of the figth*****"
        
dog1 = Dog("Spike",8,150)
dog2 = Dog("Butcher",5,180)
dog3 = Dog("Fuckface",2,120)

print(dog1.figth(dog2))



# EXERCISE 3




            

        






    


  