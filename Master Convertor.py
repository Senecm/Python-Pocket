import sys
from time import sleep
__Author__ = "Toenail"
__Lisence__ = "Unliscenced", False
__Property__ = "For"
    #exit protocol
def userExit():
    while True:
        user_exit = input("Input Q to quit or M to return to the main menu: ")
        if user_exit == "Q":
            print("Guten tag")
            sys.exit(0)
        elif user_exit == "M":
            break
        else: 
            print("Invalid response... returning...")
while True:
    print("Hello, conversions are listed below:")
    sleep(1)
    print(
        '''
        1. Length
        2. Weight
        3. Time
        '''
    )
    sleep(1)
    user_choice = int(input("choose (1/2/3): "))
    #Length
    if user_choice == 1:
        print(
            '''
            Length conversion options:

            mm to cm
            mm to m
            mm to km

            cm to mm
            cm to m
            cm to km

            m to mm
            m to cm
            m to km

            km to mm
            km to cm
            km to m
            '''
        )
        #user input
        user_input = input("Select an option: ")
        def choiceOne(option):
            options = {
                #mm
                "one": "mm to cm",
                "two": "mm to m",
                "three": "mm to km",
                #cm
                "four": "cm to mm",
                "five": "cm to m",
                "six": "cm to km",
                #m
                "seven": "m to mm",
                "eight": "m to cm",
                "nine": "m to km",
                #km
                "ten": "km to mm",
                "eleven": "km to cm",
                "twelve": "km to m"
            }
            #user number
            user_num = int(input("Inptut in your number: "))
            #mm
            if user_input == options["one"]:
                print(user_num / 10)
            elif user_input == options["two"]:
                print(user_num / 1000)
            elif user_input == options["three"]:
                print(user_num / 1000000)
            #cm
            elif user_input == options["four"]:
                print(user_num * 10)
            elif user_input == options["five"]:
                print(user_num / 100)  
            elif user_input == options["six"]:
                print(user_num / 1000)
            #m
            elif user_input == options["seven"]:
                print(user_num * 1000)
            elif user_input == options["eight"]:
                print(user_num * 100)
            elif user_input == options["nine"]:
                print(user_num / 100)
            #km    
            elif user_input == options["ten"]:
                print(user_num * 1000000)
            elif user_input == options["eleven"]:
                print(user_num * 10000)
            elif user_input == options["twelve"]:
                print(user_num / 1000)
            else:
                print("Invalid response.. returning...")
                return     

        #calling the function
        choiceOne(user_input)
        userExit()
        
    elif user_choice == 2:
        print(
            '''
            Weight conversion options:

            mg to g
            mg to kg

            g to mg
            g to kg

            kg to mg
            kg to g
            '''
        )
        #user input
        user_input = input("Select an option: ")
        def choiceTwo(option):
            #mg
            options = {
                #mg
                "one": "mg to g",
                "two": "mg to kg",
                #g
                "three": "g to mg",
                "four": "g to kg",
                #kg
                "five": "kg to mg",
                "six": "kg to g"            
            }
            #user_number
            user_num = int(input("Input your number: "))
            if user_input == options["one"]:
                print(user_num / 1000)
            elif user_input == options["two"]:
                print(user_num / 1,000,000)
            elif user_input == options["three"]:
                print(user_num * 1000)
            elif user_input == options["four"]:
                print(user_num / 1000)
            elif user_input == options["five"]:
                print(user_num * 1,000,000)
            elif user_input == options["six"]:
                print(user_num * 1000)
        choiceTwo(user_choice)
        userExit()
    #Time 
    elif user_choice == 3:
        print(
            '''
            Time conversion options:

            ms to s
            ms to m
            ms to hr

            s to ms
            s to m
            s to hr

            m to ms
            m to s
            m to hr

            hr to ms
            hr to s
            hr to m
            '''
        )
        #user input
        user_input = input("Select an option: ")
        def choiceThree(option):
            options = {
                #ms
                "one": "ms to s",
                "two": "ms to m",
                "three": "ms to hr",
                #s
                "four": "s to ms",
                "five": "s to m",
                "six": "s to hr",
                #m
                "seven": "m to ms",
                "eight": "m to s",
                "nine": "m to hr",
                #hr
                "ten": "hr to ms",
                "eleven": "hr to s",
                "twelve": "hr to m"
            }
            #user number
            user_num = int(input("Input your number: "))
            '''
            for key in options:
                if user_input == options[key]
            '''
            #ms
            if user_input == options["one"]:
                print(user_num / 1000)
            elif user_input == options["two"]:
                print(user_num / 60000)
            elif user_input == options["three"]:
                print(user_num / 3,600,000)
            #s
            elif user_input == options["four"]:
                print(user_num * 1000)
            elif user_input == options["five"]:
                print(user_num / 60)  
            elif user_input == options["six"]:
                print(user_num / 3600)
            #m
            elif user_input == options["seven"]:
                print(user_num * 60000)
            elif user_input == options["eight"]:
                print(user_num * 60)
            elif user_input == options["nine"]:
                print(user_num / 60)
            #hr    
            elif user_input == options["ten"]:
                print(user_num * 3,600,000)
            elif user_input == options["eleven"]:
                print(user_num * 3600)
            elif user_input == options["twelve"]:
                print(user_num * 60)
            else:
                print("Invalid response.. returning...")
                return
        #calling the function
        choiceThree(user_input)
        userExit()
    else: 
        print("Thats not a valid number!\n")
        sleep(0.5)
        print("Returning...")
        sleep(0.5)

 