# daily challenge
# 1
user_string = input("Write a string \n")

if len(user_string) < 10:
    print("string not too long")

elif len(user_string) > 10:
    print("string too long")

else:
    print("perfect string")

# 2


print(user_string[0])
print(user_string[len(user_string)-1])


# 3
for i in user_string:
    print(i)
