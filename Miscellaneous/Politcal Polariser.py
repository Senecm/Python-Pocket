__author__ = "Gordon"

#imports
# import pygame

#polarising variables
left_sway = 0
right_sway = 0
auth_sway = 0
lib_sway = 0

#
#validation
def InvalidInput():
    print("The input you entered is invalid.")
    userQuit = input("quit (Y/N) ")
    if userQuit == "Y":
        quit(0)
    elif userQuit == "N":
        return
    else:
        print("Invalid input, quitting...")
        quit(0)
#mainloop
while True:
    print("Welcome to the Political Polariser")
    print("To answer a question type 'A' or 'D' (agree or disagree respectivley)")

    #user_choice = input("Would you like to take the short or long test?")
    print("loading questions...")

    userInput = print("In a world with increasingly diverese opinions, it is better for the state to make most of the important descisions.\n")
    if userInput == "A":
        auth_sway + 0.5
    elif userInput == "D":
        lib_sway - 0.5
    else:
        InvalidInput()
    userInputOne = input("Intervention in the economy should be kept to a minimum.")
    if userInput == "A":
        auth_sway + 0.5
        right_sway - 0.5
    elif userInput == "D":
        lib_sway - 0.5
        left_sway - 0.5
    else:
        InvalidInput()
    userInputTwo = input("The majority cannot be trusted.")
    if userInput == "A":
        auth_sway + 1
    elif userInput == "D":
        lib_sway - 1
    else:
        InvalidInput()
    userInputThree = input("Democratic values must be safeguarded at all costs, even if it means challenging radical parties.")
    if userInput == "A":
        auth_sway + 0.5
    elif userInput == "D":
        lib_sway - 0.5
    else:
        InvalidInput()

    #exit handler
#relaying the results
# pygame.init()
