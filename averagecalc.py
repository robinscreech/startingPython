# userInput = input('Enter a set of numbers: ')
#
# def genAvg(setOfNumbers):
#     sumOfNumber = 0
#
#     for value in userInput:
#         sumOfNumber += value
#         totalAverage = sumOfNumber / len(userInput)
#
#     print('The total sum is: ', sumOfNumber)
#     print('The total avg is: ', totalAverage)
#
# genAvg(userInput)

numbers = []
totalSum = 0

while (True):
    val = input('Please add numbers or (press \'q\' when done) : ')
    if val == 'q':
        return false
    else:
        for number in numbers:
            totalSum += numbers[number]
            print ('Total', totalSum)        
        numbers.append(int(val))

print(numbers)
