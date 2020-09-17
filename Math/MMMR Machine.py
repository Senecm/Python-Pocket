__author__ = "Gordan"

def user_exit():
    user_choice = input("Quit (Y/N)")
    if user_choice == "Y":
        print("goodbye")
        quit(0)
    elif user_choice == "N":
        print("returning to main menu...")
        return
while True:
    print("Welcome to the Mean Median Mode and Range machine!")
    user_input = int(input("Input the number of numbers (haha, funny) in your list: "))
    num_lst = []
    for i in range(user_input):
        numbers = int(input("Enter a number: "))
        num_lst.append(numbers)
    #caculation function
    def Mean():
        mean = sum(num_lst) / len(num_lst)
        return mean
    def Median():
        num_lst_sorted = sorted(num_lst)
        median = (len(num_lst_sorted) + 1) / 2
        return median
    def Mode():
        for i in range(user_input):
            if num_lst.count(i) > 1:
                mode = i
                return mode
    def Range():
        num_lst_sorted = sorted(num_lst)
        lowest_num = num_lst_sorted[0]
        highest_num = num_lst_sorted[-1]
        Range = highest_num - lowest_num
        return Range
    #printing the values
    print("Mean:", Mean())
    print("Median:", Median())
    print("Mode", Mode())
    print("Range:", Range())
    #calling the exit function
    user_exit()