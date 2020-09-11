__author__ = "Kevin"
__licsence__ = "unlicsenced"

import webbrowser as wb
from time import sleep
while True:
    user_input = input("Enter a name of a song: ")
    print("openin in new tab...")
    wb.open('https://genius.com/search?q='+user_input, new=2)
    user_choice = input("Are you satisfied with your result (Y/N): ")
    if user_choice == "Y":
        print("Great!")
    elif user_choice == "N":
        print("Sorry to hear that!\n")
        sleep(0.8)
        print("Rerouting and searching through google...")
        sleep(0.8)
        wb.open('https://google.com/search?q='+user_input+'(song)', new=2)
    user_exit = input("Exit(Y/N)?")
    if user_exit == "Y":
        break
#browser_function = int(input("Press 1 to open a new window, and 2 to open a new tab: "))#######################
#if browser_function == 1:
    #webbrowser.open('https://genius.com/search?q='+user_input, new=1)                        ####################
#elif browser_function == 2:                                                                  Chrome Prevents THis
    #webbrowser.open('https://genius.com/search?q='+user_input, new=2)                        ####################