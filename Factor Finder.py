__author__ = "Toenail"
__license__ = "Unlicensed"
__property__ = "For"

print("Welcome to factor finder\n")
user_num = int(input("Please enter a number: "))
#main function
def find_factors(number):
   for i in range(1, number + 1):
       if number % i == 0:
           print(i)
find_factors(user_num)


