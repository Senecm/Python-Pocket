__author__ = "Gordon"

#imports
import pygame

#polarising variable
LEFTRIGHTSWAY = 0
AUTHLIBSWAY = 0

#exit protocol
def UserExit():
    userQuit = input("quit (Y/N) ")
    if userQuit == "Y":
        quit(0)
    elif userQuit == "N":
        return
    else:
        print("Invalid input, quitting...")
        quit(0)
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
print("Welcome to the Political Polariser")
print("To answer a question type 'A' or 'D' (agree or disagree respectivley)")

#user_choice = input("Would you like to take the short or long test?")
print("loading questions...")

while True:
    userInput = input("In a world with increasingly diverese opinions, it is better for the state to make most of the important descisions. ")
    if userInput == "A":
        AUTHLIBSWAY += 0.5
    elif userInput == "D":
        AUTHLIBSWAY -= 0.5
    else:
        InvalidInput()
    userInputOne = input("Intervention in the economy should be kept to a minimum. ")
    if userInputOne == "A":
        AUTHLIBSWAY + 0.5
        LEFTRIGHTSWAY - 0.5
    elif userInputOne == "D":
        AUTHLIBSWAY - 0.5
        LEFTRIGHTSWAY - 0.5
    else:
       InvalidInput()
    userInputTwo = input("The majority cannot be trusted. ")
    if userInputTwo == "A":
        AUTHLIBSWAY + 1
    elif userInputTwo == "D":
        AUTHLIBSWAY - 1
    else:
        InvalidInput()
    userInputThree = input("Democratic values must be safeguarded at all costs, even if it means challenging radical parties. ")
    if userInputThree == "A":
        AUTHLIBSWAY + 2
        LEFTRIGHTSWAY + 0.5
    elif userInputThree == "D":
        AUTHLIBSWAY - 2
        LEFTRIGHTSWAY - 0.5
    else:
        InvalidInput()
    userInputFour = input("The government always knows best.")
    if userInputThree == "A":
        AUTHLIBSWAY + 2
        LEFTRIGHTSWAY + 0.5
    elif userInputThree == "D":
        AUTHLIBSWAY - 2
        LEFTRIGHTSWAY - 0.5
    else:
        InvalidInput()
    #UserExit()
    #relaying the results
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Political Polariser")

    #drawing the plane
    pygame.draw.line(win, (255, 255, 255), (100, 100), (0, 500), width=4)
    pygame.display.flip()
    #main loop
    status = True
    while status:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
    pygame.quit()