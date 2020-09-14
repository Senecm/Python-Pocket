# Constants,
## Constant pieces of code you may find throughout my projects:

### user_exit
```
def user_exit():
    user_choice = input("quit (Y/N): ")
    if user_choice == "Y":
        print("goodbye")
        sys.exit(0)
    elif user_choice = "N"
        print("returning to main menu...")
        return
    else:
        print("could not understand")
        return

```
This is a simple function, which is called by the main loop of the code to ask the user to exit. If they respond with yes, the function quits the python interpreter using `sys.exit(0)` from the `sys` module. If they respond with no, the function breaks and the main loop is initiated again. If they input a value which is neither, the program will then return to the main menu.