user_input = input("write a sentence without a \n")


if not "a" in user_input and len(user_input) + 1 > len(user_input):
    print("Congratulations")
else:
    print("try again")
