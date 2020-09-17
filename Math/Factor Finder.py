__author__ = "Gordan"

def user_exit():
    user_choice = input("quit (Y/N): ")
    if user_choice == "Y":
        quit(0)
    elif user_choice == "N":
        return
    else:
        print("cannot understand, returning to main menu...")
        return
print("Welcome to factor finder\n")
user_num = int(input("Please enter a number: "))
#main function
def find_factors(number):
   for i in range(1, number + 1):
       if number % i == 0:
           print(i)
find_factors(user_num)


