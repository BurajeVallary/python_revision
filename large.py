# # Write a python program that will accept an array
# # of numbers and print out the largest and smallest no.

def largest_smallest_numbers(*numbers):
    smallest = largest = numbers[0]

 
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    print("Smallest number:", smallest)
    print("Largest number:", largest)


def min_max(numbers):
    numbers.sort()
    smallest = numbers[0]
    largest = numbers[-1]
    print("Smallest number:", smallest)
    print("Largest number:", largest)

numbers = [123, 450, 67, 126, 8, 364, 856]

min_max(numbers)    


#even numbers

def sum_numbers(nums):
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
            print(sum)



def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True



# Write a Python program that uses a dictionary to count the
#  frequency of each character in a given string.

test_str = "Hello Good Morning this is going to be a good day"

# using naive method to get count
# of each element in string
count = {}

for i in test_str:
	if i in count:
		count[i] += 1
	else:
		count[i] = 1

print("Count of all characters in GeeksforGeeks is :\n "
	+ str(count))


def count_char(string):
    freq_dict ={ }
    for x in string:
        if x in freq_dict:
            freq_dict[x]+=1
        else:
            freq_dict[x]=1
    return freq_dict




