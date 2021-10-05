def main():
    password=get_password()
    print_asterisks(password)
def get_password():
     getpassword=input("What's your password?")
     while (len(getpassword) < 6):
         getpassword = input("the length can not be less than 6!your password is")
     return getpassword
def print_asterisks(password):
    for i in range(0, len(password), 1):
        print("*", end="")
main()

