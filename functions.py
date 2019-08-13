# def numbers(number):
#     num = 0
#     while (num <= number):
#         print(num)
#         num += 1
#
# numbers(5)

def numbers(number):
    num = 0
    while (num <= number):
        print(num)
        num += 1

def call_numbers(num_function, limit):
    num_function(limit)

func = numbers
upper = 15

call_numbers(func, upper)
