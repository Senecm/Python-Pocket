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
            #mm
            op_one = "mm to cm"
            op_two = "mm to m"
            op_three = "mm to km"
            #cm
            op_four = "cm to mm"
            op_five = "cm to m"
            op_six = "cm to km"
            #m
            op_seven = "m to mm"
            op_eight = "m to cm"
            op_nine = "m to km"
            #km
            op_ten = "km to mm"
            op_eleven = "km to cm"
            op_twelve = "km to m"
            #user number
            user_num = int(input("Inptut in your number: "))
            #mm
            if user_input == op_one:
                print(user_num / 10)
            elif user_input == op_two:
                print(user_num / 1000)
            elif user_input == op_three:
                print(user_num / 1000000)
            #cm
            elif user_input == op_four:
                print(user_num * 10)
            elif user_input == op_five:
                print(user_num / 100)  
            elif user_input == op_six:
                print(user_num / 1000)
            #m
            elif user_input == op_seven:
                print(user_num * 1000)
            elif user_input == op_eight:
                print(user_num * 100)
            elif user_input == op_nine:
                print(user_num / 100)
            #km    
            elif user_input == op_ten:
                print(user_num * 1000000)
            elif user_input == op_eleven:
                print(user_num * 10000)
            elif user_input == op_twelve:
                print(user_num / 1000)
            else:
                print("Invalid response.. returning...")
                return     

        #calling the function
        choiceOne(user_input)
        userExit()
        
    elif user_choice == 2:
        print("Weight conversion options")
        print("mg to g")
        print("g to kg")
        print("")
        print("g to mg")
        print("g to kg")
        print("")
        print("kg to mg")
        print("kg to g")
        print("")
        #user input
        user_input = input("Select an option: ")
        def choiceTwo(option):
            #mg
            op_one = "mg to g"
            op_two = "g to kg"
            #g
            op_three = "g to mg"
            op_four = "kg to g"
            #kg
            op_four = "kg to mg"
            op_five = "kg to g"
            #user_number
            user_num = int(input("Input your number: "))
            if user_input == op_one:
                print(user_num / 1000)
            elif user_input == op_two:
                print(user_num / 1000)
            elif user_input == op_three:
                print(user_num * 100)
            elif user_input == op_four:
                print(user_num * 1000000)
            elif user_input == op_five:
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
            #ms
            op_one = "ms to s"
            op_two = "ms to m"
            op_three = "ms to hr"
            #s
            op_four = "s to ms"
            op_five = "s to m"
            op_six = "s to hr"
            #m
            op_seven = "m to ms"
            op_eight = "m to s"
            op_nine = "m to hr"
            #hr
            op_ten = "hr to ms"
            op_eleven = "hr to s"
            op_twelve = "hr to m"
            #user number
            user_num = int(input("Input your number: "))
            #ms
            if user_input == op_one:
                print(user_num / 1000)
            elif user_input == op_two:
                print(user_num / 60000)
            elif user_input == op_three:
                print(user_num / 3,600,000)
            #s
            elif user_input == op_four:
                print(user_num * 1000)
            elif user_input == op_five:
                print(user_num / 60)  
            elif user_input == op_six:
                print(user_num / 3600)
            #m
            elif user_input == op_seven:
                print(user_num * 60000)
            elif user_input == op_eight:
                print(user_num * 60)
            elif user_input == op_nine:
                print(user_num / 60)
            #hr    
            elif user_input == op_ten:
                print(user_num * 3,600,000)
            elif user_input == op_eleven:
                print(user_num * 3600)
            elif user_input == op_twelve:
                print(user_num * 60)
            else:
                print("Invalid response.. returning...")
                return
        #calling the function
        choiceThree(user_input)
        userExit()





 