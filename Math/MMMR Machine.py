__author__ = "Kevin"
__liscence__ = "unliscenced"

print("Welcome to the Mean Median Mode and Range machine!")
try:
    user_list = str(input("Please input your numbers: ")).split(" ")
    for item in range(len(user_list)):
        user_list[item] = int(user_list[item])
except Exception as e:
    print("Error occured:\n"+e)
    quit(0)

print("What operation do you want to do:\nMean\nMedian\nMode\nRange")
choices = ["Mean", "Median", "Mode", "Range"]

while True:
    operation = str(input("Please choose out of the 4 options above, or type Quit to quit: "))
    if operation == "Quit":
        quit(0)
    elif operation == "Mean":
        answer = 0
        for number in user_list:
            answer += number
        answer = answer / len(user_list)
        print("Ok, the mean of your list is: "+str(answer))
    elif operation == "Median":
        sortedList = sorted(user_list)
        listLen = len(sortedList)
        index = (listLen - 1) // 2
        if listLen % 2:
            answer = sortedList[index]
        else:
            answer = (sortedList[index] + sortedList[index + 1]) / 2.0
        print("Ok, the median of your list is: "+str(answer)) #https://stackoverflow.com/a/24101534/14128844
    elif operation == "Mode":
        answer = max(set(user_list), key=user_list.count)
        print("Ok, the mode of your list is: "+str(answer))
    elif operation == "Range":
        user_list_temp = sorted(user_list)
        answer = user_list_temp[len(user_list_temp) - 1] - user_list_temp[0]
        print("Ok, the range of your list is: "+str(answer))
    else:
        print("Input "+str(operation)+" is not valid, try again.")
