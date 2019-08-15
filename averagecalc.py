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
        break
    else:
        numbers.append(int(val))
        print("Number accepted, continue adding or press Q to submit & quit")

for number in numbers:
    totalSum += number

totalSum = totalSum / len(numbers)
print ('Total average of your numbers is {0:.0f} '.format(totalSum))
