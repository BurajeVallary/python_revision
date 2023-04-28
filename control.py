
# Write a function that uses while, if and continue statements to 
# print all the even numbers between 0 and 50. 


def even_numbers():
    i = 0
    while i <= 50:
        if i % 2 != 0:
            i += 1
            continue
        print(i)
        i += 1
    


#  Write a function that takes an integer argument and prints "Prime" if 
# the number is prime, and "Not prime" if the number is not prime.     

def prime_number(z):
    if z <= 1:
        print("Not prime")
       
    for i in range(2, int(z**0.5) + 1):
        if z % i == 0:
            print("Not prime")
           
    print("Prime")



# Write a function that takes a list of integers as input and 
# prints the sum of all the even numbers in the list.


def sum_of_even_numbers(list):
    sum = 0
    for num in list:
        if num % 2 == 0:
            sum += 1
    print(sum)

list=[2,1,2]
sum_of_even_numbers(list)



# Write a function that takes any two integers as input, and 
# prints the sum of all the numbers between the two integers 
# (inclusive) that are divisible by 3.


def sum_divisible_by_three(x, y):
    if x > y:
        x, y = y, x
    total = 0  
    for i in range(x, y+1):  
        if i % 3 == 0:
            total += i
            print(total)
    
sum_divisible_by_three(2, 10)    
  
        
            
    
 
 
  





