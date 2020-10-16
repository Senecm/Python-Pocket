__author__ = "Gordan"
__author__ = "Sebby37"
#imports
import os
#introduction
print("Welcome.\n")
print("This program walks you through a set up process to convert your algebraic notation into PGN format.\n")
print("Converts your written games into PGN to be analyised")

UserInput = int(input("Input 1 to input data directly into a pgn and 2 to convert a txt file to pgn: "))
if UserInput == 1:
    #naming the file
    filename = str(input("Name your file: "))
    #gathering user input 
    user_inputs = []
    print("\nThe following will prompt you to input data, type \"D\" (done) when your finished \n")
    Event = input("event: ") #name of event
    Site = input("site: ") #city, region COUNTRY
    Date = input("date: ") #YYYY/MM/DD
    Round = input("round: ") #round number
    White = input("white: ") #lastname, firstname
    Black = input("black: ") #lastname, firstname
    Result = input("result: ") #whites score [- or *] blacks score
    while True:
        user_input = str(input("Input your data: "))
        if user_input == "D":
            break
        #Code to write the final inputs to the list, will probably be function to determine what the final result will be
        user_inputs.append(user_input)
    with open(f"Chess/{filename}.pgn", "w+") as o:
        o.truncate(0)
        o.write(f'[Event "{Event}"]\n')
        o.write(f'[Site "{Site}"]\n')
        o.write(f'[Date "{Date}"]\n')
        o.write(f'[Round "{Round}"]\n')
        o.write(f'[White "{White}"]\n')
        o.write(f'[Black "{Black}"]\n')
        o.write(f'[Result "{Result}"]\n\n')
        for i in range(len(user_inputs)):
            o.write(f"{i+1}. {user_inputs[i]} ")
        o.close()
elif UserInput == 2:
    FILENAME = str(input("Name of the file: "))
    DIRECTORY = str(input("Specify the directory: (type $ if it is in the current directory): "))
    if DIRECTORY != "$":
        print(DIRECTORY)
        try:
            with open(f"{FILENAME}.txt", "r") as o:
                file = o.read()
                print(file)
        except Exception as e:
            quit(e)
    else:
        #curDir = os.getcwd()
        curDir = os.path.dirname(os.path.realpath(f"{FILENAME}.txt"))
        print(curDir)
        #getting the currant directory
        try:
            with open(f"{FILENAME}.txt", "r") as o:
                file = o.read()
                print(file)
        except Exception as e:
            quit(e)


    '''
    fileDir = os.path.dirname(os.path.realpath(f"{filename}.txt"))
    print(fileDir)
    '''
    #with open(f"")
