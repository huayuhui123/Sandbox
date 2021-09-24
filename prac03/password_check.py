password = input("What's your password?")
while (len(password) < 6):
    password = input("the length can not be less than 6!your password is")
for i in range(0, len(password), 1):
    print("*", end="")
