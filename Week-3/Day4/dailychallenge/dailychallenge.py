
class Text:
  def __init__(self,string = "A good book would sometimes cost as much as a good house."):
    self.string = string

  from collections import Counter


  def freq_word(self,word):
      from collections import Counter
      freq_of_word = self.string.split(' ')
      if word in freq_of_word:
        count_word = Counter(freq_of_word)
        print(f"{word} frecuency is {count_word[word]}")
      else:
       print("That word is not in the text")
  
  def common_word(self):
    sentence = self.string.split(' ')
    count_times_word = {}
    for word in sentence:
      count_times_word[word] = count_times_word.get(word,0) + 1
    max_word_ocurrs = max(count_times_word.values())
    for index,value in count_times_word.items():
      if value == max_word_ocurrs:
        return (f"The most common word in the text is {index} , appears {value} times")
      
  def unique_words(self):
    list_of_words = self.string.split(' ')
    unique_word = list_of_words[0]
    unique_words_list = [unique_word]
    for word in list_of_words:
      if word != unique_word:
        unique_word = word
        unique_words_list.append(word)
    print(unique_words_list)      


#  2 
  @classmethod

  def text_from_file(cls,text):
    with open("the_stranger.txt","r") as text:
      text_from_file = text.read()
      return cls(text_from_file)
    
read_text = Text.text_from_file("the_stranger.txt")
print(read_text)
    

    

    













frase1 = Text("Today is a a a happy day")

frase1.freq_word("a")

print(frase1.common_word())

frase1.unique_words()      


       
      
          
      
    

  
    
    
  



    
      
      
    


  
