userInput = input('Enter a set of numbers: ')

def genAvg(setOfNumbers):
    sumOfNumber = 0

    for value in userInput:
        sumOfNumber += value
        totalAverage = sumOfNumber / len(userInput)

    print('The total sum is: ', sumOfNumber)
    print('The total avg is: ', totalAverage)

genAvg(userInput)

enterNumber = 1279.00 / 100 * 17
print('The dis is {0:.2f}'.format(enterNumber))
