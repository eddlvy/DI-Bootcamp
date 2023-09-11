from exerciseXP import Dog
import random


class Petdog(Dog):
  def __init__(self,name,age,weigth,trained = False):
    super().__init__(name,age,weigth)
    self.trained = trained
   
  def train(self):
    self.trained = True
    print(f"{super().bark()}")

  def play(self,*dog_names):
    list_of_dogs = []
    list_of_dogs.extend(dog_names)
    return (f"{' , '.join(list_of_dogs)} all play together")

  def do_a_trick(self):

    sentences = [(f"{self.name} does a barrel roll"),
      (f"{self.name} stands on his back legs"),
      (f"{self.name} shakes your hand"),
      (f"{self.name} plays dead")]
    if not self.trained:
     return random.choice(sentences)  
    
    
    

dog5 = Petdog("Jaws",12,120)

print(dog5.play("Lucky","Butcher","Dracula"))

print(dog5.do_a_trick())
      
    
    



   

  

