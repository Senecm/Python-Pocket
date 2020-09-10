__author__ = "Toenail"
__license__ = "Unlicensed"
__property__ = "For"

#main function
def find_factors(number):
   return " ".join([str(i) for i in range(1, number+1) if number % i == 0])

find_factors(int(input("Welcome to factor finder\n\nPlease enter a number: ")))
