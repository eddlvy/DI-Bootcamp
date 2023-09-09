# CHALENGE 1

def sort_list_alphabetically ():
  user_input = input("write words separated by a comma\n")
  user_list_sorted = [ sorted(word for word in user_input.split(","))]
  print(user_list_sorted)
  
sort_list_alphabetically()

# CHALLENGE 2

def longest_word(sentence):
  sentence_string = f"{sentence}"
  sentence_list_words = [word for word in sentence_string.split(" ")]
  longest_word_in_string = sentence_list_words[0]
  max_len = len(sentence_list_words[0])
  for index,word in enumerate(sentence_list_words):
    if len(word) > max_len:
      max_len = len(word)
      longest_word_in_string = word
    else:
      pass 

  print(longest_word_in_string)
  
  
      

longest_word("It's a longest sentence")
  
  
    

  
  
  



