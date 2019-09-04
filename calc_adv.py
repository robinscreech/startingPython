class Calc:

    list = []
    def __init__(self, first, second, action):
        total = 0


    def addition(previousNum, currentNum):
        total = previousNum + currentNum
        print("Total : " + str(total))

    def subtraction(previousNum, currentNum):
        total = previousNum - currentNum
        print("Total : " + str(total))

    def division(previousNum, currentNum):
        total = previousNum / currentNum
        print("Total : " + str(total))

    def multi(previousNum, currentNum):
        total = previousNum * currentNum
        print("Total : " + str(total))

    getValue = input("Please enter your numbers (q to quit):")

    sums = getValue.split(" ")
    print(sums)

    if sums[1] == "+":
        addition(int(sums[0]), int(sums[2]))
    elif sums[1] == "-":
        subtraction(int(sums[0]), int(sums[2]))
    elif sums[1] == "/":
        division(int(sums[0]), int(sums[2]))
    else:
        multi(int(sums[0]), int(sums[2]))
