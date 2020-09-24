__author__ = "Gordon"
__author__ = "Sebba37"

#imports
import pygame
import random
import ideologies  
                            #testing
#polarising variable
LEFTRIGHTSWAY = 250
AUTHLIBSWAY = 250

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
        AUTHLIBSWAY += 5
    elif userInput == "D":
        AUTHLIBSWAY -= 5
    else:
        InvalidInput()
    userInputOne = input("Intervention in the economy should be kept to a minimum. ")
    if userInputOne == "A":
        AUTHLIBSWAY += 5
        LEFTRIGHTSWAY -= 5
    elif userInputOne == "D":
        AUTHLIBSWAY -= 5
        LEFTRIGHTSWAY -= 5
    else:
       InvalidInput()
    userInputTwo = input("The majority cannot be trusted. ")
    if userInputTwo == "A":
        AUTHLIBSWAY += 10
    elif userInputTwo == "D":
        AUTHLIBSWAY -= 10
    else:
        InvalidInput()
    userInputThree = input("Democratic values must be safeguarded at all costs, even if it means challenging radical parties. ")
    if userInputThree == "A":
        AUTHLIBSWAY += 20
        LEFTRIGHTSWAY += 5
    elif userInputThree == "D":
        AUTHLIBSWAY -= 20
        LEFTRIGHTSWAY -= 5
    else:
        InvalidInput()
    userInputFour = input("The government always knows best. ")
    if userInputThree == "A":
        AUTHLIBSWAY += 20
        LEFTRIGHTSWAY += 5
    elif userInputThree == "D":
        AUTHLIBSWAY - 20
        LEFTRIGHTSWAY - 5
    else:
        InvalidInput()
    userInputFive = input("Privatisation of industry benefites all people. ")
    if userInputThree == "A":
        AUTHLIBSWAY -= 10
        LEFTRIGHTSWAY += 20
    elif userInputThree == "D":
        AUTHLIBSWAY += 5
        LEFTRIGHTSWAY -= 20
    else:
        InvalidInput()
    userInputSix = input("Globilisation is inherently evil. ")
    if userInputThree == "A":
        AUTHLIBSWAY += 5
        LEFTRIGHTSWAY -= 10
    elif userInputThree == "D":
        AUTHLIBSWAY += 5
        LEFTRIGHTSWAY += 5
    else:
        InvalidInput()

    #final results calculation
    print(f"Your social scale is: {AUTHLIBSWAY}")
    print(f"Your economic sway is: {LEFTRIGHTSWAY}")
    #UserExit()
    #relaying the results    
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Political Polariser")
    
        #################REFERENCING###########################
    '''
    #0,0
    pygame.draw.circle(win, (0, 0, 0), (0, 0), 15)
    #250,250
    pygame.draw.circle(win, (0, 0, 0), (250, 250), 15)
    #500,500
                                    #looks ugly, use only when needed
    pygame.draw.circle(win, (0, 0, 0), (500, 500), 15)
    '''
    #top of screen
    pygame.draw.circle(win, (0, 0, 0), (250, 0), 15)
    #bottom of screen
    pygame.draw.circle(win, (0, 0, 0), (250, 500), 15)
    #middle left of screen
    pygame.draw.circle(win, (0, 0, 0), (0, 250), 15)
    #middle right of screen
    pygame.draw.circle(win, (0, 0, 0), (500, 250), 15)

    ###########################colouring the quadrants###############################
    #Auth right quadrant
    authRightCol = (0, 0, 255)
    pygame.draw.rect(win, authRightCol, (250, 0, 500, 250))
    #Auth left quadrant
    authLeftColours = (255, 0, 0)
    pygame.draw.rect(win, authLeftColours, (0, 0, 250, 250))
    #Lib left quadrant
    libLeftColours = (0, 255, 0) #NO STOP, trust me ive got this
    pygame.draw.rect(win, libLeftColours, (0, 250, 250, 250))
    #lib right quadrant
    #pygame.draw.rect(win, (255, 255, 0), (250, 250, 500, 500))
    libRightColours = [(255, 255, 0), (213, 0, 255)]
    pygame.draw.rect(win, random.choice(libRightColours), (250, 250, 500, 500))

    ###########################plotting user input##################
    pygame.draw.circle(win, (0, 0, 0), (int(LEFTRIGHTSWAY), int(AUTHLIBSWAY)), 5)
    #pygame.draw.circle(win, (0, 0, 0), (275, 265), 15)# debuging 
    
    ###########drawing the cartisean plane#########
    ###############################################
    #Y
    pygame.draw.line(win, (0, 0, 0), (250, 0), (250, 500), 5)
    #X
    pygame.draw.line(win, (0, 0, 0), (0, 250), (500, 250), 5)
    pygame.display.flip()
    
    #################drawing the grid#########
    for x in range(0, 500): 
        if x % 20 == 0:
            pygame.draw.line(win, (125, 125, 125), (x, 0), (x, 500))
            pygame.display.flip()
    
    for y in range(0, 500):
        if y % 20 == 0:
            pygame.draw.line(win, (125, 125, 125), (0, y), (500, y))
            pygame.display.flip()
    
    #pygame.draw.circle(win, (0, 0, 0), (50, 50), 15)
    #main loop
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
                break
    pygame.quit()
    
    #ideological info
    def InfoRelay():
        #creating an instants of the classes
        PLANE = ideologies.Plane()
        PILLARS = ideologies.Pillars()
        print(
        '''
        1. Info about the plane
        2. Info about the quadrants
        3. Info about the ideologies
        '''
        )
        user_info_choice = input("pick an option: ")
        if user_info_choice == 1:
            PLANE.plane()
        elif user_info_choice == 2:
            PLANE.quadrants()
        elif user_info_choice ==3:
            print(
                '''
                1. Info about communism
                2. Info about fascism
                3. Info about authoritarianism
                4. Info about libertarianism
                '''
            )
            user_info_ideology = input("pick an option: ")
            if user_info_ideology == 1:
                PILLARS.communism()
            elif user_info_ideology == 2:
                PILLARS.fascism()
            elif user_info_ideology == 3:
                PILLARS.authoritarianism()
            elif user_info_ideology == 4:
                PILLARS.libertarianism()
            else:
                UserExit()

    user_info_exit = input("Want to know more (Y/N)? ")
    if user_info_exit == "Y":
        InfoRelay()
    elif user_info_exit == "N":
        print("Goodbye...")
        quit(0)
    else:
        UserExit()
