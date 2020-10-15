__author__ = "Gordan"
__author__ = "Sebby37"
#import notation
#import PGN
#introduction
print("Welcome.\n")
print("This program walks you through a set up process to convert your algebraic notation into PGN format.\n")
print("Converts your written games into PGN to be analyised")
#demo
demo = input("View info about chess notation and PGN files (Y/N)? ")
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
    o.write(f'[Result "{Result}"]\n\n') #vomit face 1
    for i in range(len(user_inputs)):
        o.write(f"{i+1}. {user_inputs[i]} ")
    o.close()
