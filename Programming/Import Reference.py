import math
import os
import random
import sys
import time
import datetime
import json
import webbrowser
import turtle
import Flask
print("welcome to the module reference...\n")
print("select an option below...\n")
print(
    '''
    1. math
    2. os
    3. random
    4. sys
    5. time
    6. datetime
    7. json
    8. webbrowser
    9. turtle
    10. Flask
    '''
)
user_input = input("Option: ")
if user_input == 1:
    for i in dir(math):
        print(i)
elif user_input == 2:  
    for i in dir(os):
        print(i)
elif user_input == 3:
    for i in dir(random):
        print(i)    
elif user_input == 4:
    for i in dir(sys):
        print(i)
elif user_input == 5:
    for i in dir(json):
        print(i)
elif user_input == 6:
    for i in dir(webbrowser):
        print(i)
elif user_input == 7:
    for i in dir(turtle):
        print(i)
elif user_input == 8:
    for i in dir(Flask):
        print (i)
