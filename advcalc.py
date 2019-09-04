class Calc:

    history = []
    def __init__(self, first, second, action):
        total = 0


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
        getValue = input("Please enter your numbers (q to quit):")

        sums = getValue.split(" ")

        print("Your sum is :" + str(doSum(int(sums[0]),int(sums[2]),sums[1])))

        history.append(doSum(int(sums[0]),int(sums[2]),sums[1]))
        print(history)

        #if getValue == "q"
        break
