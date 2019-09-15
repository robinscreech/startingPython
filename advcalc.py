class Calc:

    history = []
    firstInput = False
    def __init__(self, first, second, action):
        emptyVal = 0

    def doSum(previousNum, currentNum, operator):
        if operator == "+":
            total = previousNum + currentNum
            return total
        elif operator == "-":
            total = previousNum - currentNum
            return total
        elif operator == "*":
            total = previousNum * currentNum
            return total
        else:
            total = previousNum / currentNum
            return total


    while (True):
        if firstInput == False:
            getValue = input("Please enter your numbers (q to quit):")
            inputVal = getValue.split(" ")
            print("Your sum is :" + str(doSum(int(inputVal[0]),int(inputVal[2]),inputVal[1])))
            history.append(doSum(int(inputVal[0]),int(inputVal[2]),inputVal[1]))
            print(history)
            firstInput = True

        else:
            secondGetValue = input("Do some math with the last number (q to quit):")
            secondSplit = secondGetValue.split(" ")
            result = doSum(history[-1], int(secondSplit[1]), str(secondSplit[0]))
            history.append(result)
            print(history)
            print("Your sum is : " + str(result))

        # break
