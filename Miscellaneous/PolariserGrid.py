import pygame
import random
    
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Political Polariser")

# pygame.draw.circle(win, (255, 255, 255), (x, y), radius)

the_y = 0
#harverd referencing

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
pygame.draw.rect(win, random.choice(libRightColours), (250, 250, 500, 500)) #gordan making it purple

#when senec trys to put it in the for loop :())()()()()
#################REFERENCING###########################
'''
#0,0
pygame.draw.circle(win, (0, 0, 0), (0, 0), 15)
#250,250
pygame.draw.circle(win, (0, 0, 0), (250, 250), 15)
#500,500
''' #looks ugly, use only when needed
pygame.draw.circle(win, (0, 0, 0), (500, 500), 15)
#top of screen
pygame.draw.circle(win, (0, 0, 0), (250, 0), 15)
#bottom of screen
pygame.draw.circle(win, (0, 0, 0), (250, 500), 15)
#middle left of screen
pygame.draw.circle(win, (0, 0, 0), (0, 250), 15)
#middle right of screen
pygame.draw.circle(win, (0, 0, 0), (500, 250), 15)

###########drawing the cartisean plane###################
#Y
pygame.draw.line(win, (0, 0, 0), (250, 0), (250, 500), 5)
#X
pygame.draw.line(win, (0, 0, 0), (0, 250), (500, 250), 5)
pygame.display.flip()



#################drawing the grid################## # without using images :(((()))))))
'''
for i in range(0, 500): # looping down the x
    XCOOSTART = 0
    XCOOEND = 0
    pygame.draw.line(win, (255, 255, 255), (XCOOSTART, XCOOSTART), (YCOOSTART, YCOOEND))
    XCOOSTART += 1
    XCOOEND += 1
for i in range(0, 500): #looping down the y
    YCOOSTART = 0
    YCOOEND = 0
    pygame.draw.line(win, (255, 255, 255), (XCOOSTART, XCOOSTART), (YCOOSTART, YCOOEND))
    YCOOSTART += 1
    YCOOEND += 1
'''
#My (seb's b# gaming) turn #dont forget the 15 ms in my name
for x in range(0, 500): 
    if x % 20 == 0:
        pygame.draw.line(win, (125, 125, 125), (x, 0), (x, 500))
        pygame.display.flip()

for y in range(0, 500):
    if y % 20 == 0:
        pygame.draw.line(win, (125, 125, 125), (0, y), (500, y))
        pygame.display.flip()
    
###############################
####Plotting user input######
############################
#pygame.draw.circle(win, (0, 0, 0), (LEFTRIGHTSWAY, AUTHLIBSWAR), ())

#when senec trys to put it in the for loop :())()()()()
#################REFERENCING###########################
'''
#0,0
pygame.draw.circle(win, (0, 0, 0), (0, 0), 15)
#250,250
pygame.draw.circle(win, (0, 0, 0), (250, 250), 15)
#500,500
''' #looks ugly, use only when needed
pygame.draw.circle(win, (0, 0, 0), (500, 500), 15)
#top of screen
pygame.draw.circle(win, (0, 0, 0), (250, 0), 15)
#bottom of screen
pygame.draw.circle(win, (0, 0, 0), (250, 500), 15)
#middle left of screen
pygame.draw.circle(win, (0, 0, 0), (0, 250), 15)
#middle right of screen
pygame.draw.circle(win, (0, 0, 0), (500, 250), 15)

###########drawing the cartisean plane###################
#Y
pygame.draw.line(win, (0, 0, 0), (250, 0), (250, 500), 5)
#X
pygame.draw.line(win, (0, 0, 0), (0, 250), (500, 250), 5)
pygame.display.flip()

'''
# My code for cartesian plane:
pygame.draw.line(win, (255, 255, 255), (250, 0), (250, 500), 5)
pygame.draw.line(win, (255, 255, 255), (0, 250), (500, 250), 5)
'''
#main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)
            break
    '''
    pygame.draw.circle(win, (255, 255, 255), (250, the_y), 15)
    the_y += 1
    if the_y > 500:
        the_y = 0        #whats this
    pygame.draw.rectangle(win, (0, 0, 0), (0, 0), (500, 500))
    '''
pygame.quit()
quit(0)
