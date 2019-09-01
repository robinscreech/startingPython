class Calc:

    while(True):
        getValue = input ("Please enter your numbers (q to quit):")

        # there is an issue with this accepting an int, need to look
        # into the right value to put here. 
        list.append(int(getValue))

        if getValue == "q":
            print (list)
            addition(list[0], list[1])
            break
        else:
            getValue = input ("Please enter your numbers (q to quit):")

    def __init__(self, first, second, action):
        total = 0
        list = []


    def addition(previousNum, currentNum):
        total = previousNum + currentNum
        print (total)
