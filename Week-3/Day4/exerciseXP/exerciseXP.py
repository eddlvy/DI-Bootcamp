import os # operating system

# #creating a variable that stores the path of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# #using the variable to open the file (using raw string)
with open(dir_path + r"\\words.txt", "r") as f:
    words = f.readlines()
    print(words)
# 3

def get_words_from_file():
  with open("words.txt","r") as words_file:
    words = words_file.readlines()
    print(words)
    

# 4 
from random import choice

def get_random_sentence(length):
   with open("words.txt","r") as words_file:
      words = words_file.readlines()
      new_words = [item.strip() for item in words]
      random_words = []
      for _ in range(length):
         random_words.append(choice(new_words))
      return random_words
   
print(get_random_sentence(5))
    
# 5  

def create_sentence_lowercase(number_words):
   sentence = ' '.join(get_random_sentence(number_words))
   print(sentence.lower())

create_sentence_lowercase(5)

# 6

def main(x):
   print("Define how long is your sentence, choose a number between 2 and 20")
   try:
    if  int(x)<2  or int(x)>20:
       raise ValueError
       
    if not isinstance(x,int):
       raise TypeError 
   except ValueError as error:
      print(error)
      print("Wrong number, does not match rules of program")
   except TypeError as error:
      print(error)
      print("Wrong type of data , must be a whole number")
   else:
      create_sentence_lowercase(x)
   

main(19)
main(23)        



    
    
 
   
      
      
    
    
     
     
     
     
     









  
  






     




      
     
   
   


