__author__ = "Gordon"

#imports
# import pygame

#polarising variables
left_sway = 0
right_sway = 0
auth_sway = 0
lib_sway = 0

#invalid response handler
def InvalidInput():
    print("The input you entered is invalid.")
#mainloop
while True:
    print("Welcome to the Political Polariser")
    print("To answer a question type 'agree' or disagree'")

    #user_choice = input("Would you like to take the short or long test?")
    print("loading questions...")

    userInput = print("In a world with increasingly diverese opinions, it is better for the state to make most of the important descisions.\n")
    if userInput == "agree":
        auth_sway + 0.5
    elif userInput == "disagree":
        lib_sway - 0.5
    else:
        InvalidInput()
    # userInputOne = input("") 
    # userInputTwo = input("")

    #exit handler
#relaying the results
# pygame.init()
