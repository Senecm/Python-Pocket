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
    
s1 = sleep(1)
while True:
    print("Hello, choose from the list below for conversion")
    s1
    print("---1: Length")
    print("---2: Weight and Volume")
    print("---3: Time")
    s1
    print("pick one I dare you")
    user_choice = int(input("choose (1/2/3): "))

    if type(user_choice) != int:
        print("Invalid type! Enter a number!")
        cont = input("continue? Y/N")
        if cont == "Y":
            break
    #Length
    if user_choice == 1:
        print("Length conversion options:")
        print("")
        print("mm to cm")
        print("mm to m")
        print("mm to km")
        print("")
        print("cm to mm")
        print("cm to m")
        print("cm to km")
        print("")
        print("m to mm")
        print("m to cm")
        print("m to km")
        print("")
        print("km to mm")
        print("km to cm")
        print("km to m")
        print("")
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
            Weight conversion options

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
        print("Time conversion options:")
        print("")
        print("ms to s")
        print("ms to m")
        print("ms to h")
        print("")
        print("s to ms")
        print("s to m")
        print("s to h")
        print("")
        print("m to ms")
        print("m to s")
        print("m to hr")
        print("")
        print("hr to ms")
        print("hr to s")
        print("hr to m")
        print("")
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





 