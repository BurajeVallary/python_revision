# Write a program that prints all integers between 
# 100 and 125 (including 100 and 125) to the screen using a for loop. in python


def numbers():
    y=range(100,126)
    for num in y:
        print(num)

numbers() 


# Do the same as exercise 1, but this time only print those 
# numbers between 100 and 125 that are multiples of 3.


def print_multiples_of_three():
    for num in range(100, 126):
        if num % 3 == 0:
            print(num)

print_multiples_of_three()  



# Write a Python function that takes a list of numbers as input and returns the sum of
#  all the even numbers in the list, using a for loop.

def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum_even_numbers(numbers_list)
print(even_sum) 



   