# number = 0
#
# while number < 10:
#     print(number)
#     number += 1
#     if number == 5:
#         break
#
# print('The while loop has finished')

# testing out the continue keywork for looping - also adding else
# number = 0
#
# while number < 10:
#     if number == 5:
#         number += 1
#         continue
#     print(number)
#     number += 1
# else:
#     print('condition is false')
#
# print('The while loop has finished')

# breaking out of the while - skipping else and straight to print
number = 0

while number < 10:
    if number == 5:
        number += 1
        break
    print(number)
    number += 1
else:
    print('condition is false')

print('The while loop has finished')
