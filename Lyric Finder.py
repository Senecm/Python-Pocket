import webbrowser

__author__ = "Kevin"
__licsence__ = "unlicenced"
while True:
    user_input = input("Enter a name of a song: ").replace(" ", "+")
    print("openin in new tab...")
    webbrowser.open('https://genius.com/search?q='+user_input, new=2)
    user_exit = input("Exit(Y/N)?")
    if user_exit == "Y":
        break
#browser_function = int(input("Press 1 to open a new window, and 2 to open a new tab: "))
#if browser_function == 1:
    #webbrowser.open('https://genius.com/search?q='+user_input, new=1)
#elif browser_function == 2:
    #webbrowser.open('https://genius.com/search?q='+user_input, new=2)
