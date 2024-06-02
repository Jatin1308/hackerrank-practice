
# import math

# def isPrime(number):

#     for i in range(2,(number//2)+1):
#         if number%i==0:
#             return False
#     else:
#         return True


# def largestPrimeFactor(number):
#     largest= 1
#     if isPrime(number):
#         return number
    
#     for i in range(2,int(math.sqrt(number))):
#         if number%i == 0:
#             if isPrime(i):
#                 largest = max(largest,i)
    
#     return largest
    
    
# print(largestPrimeFactor(10))



def largest_prime_factor(number):
    # Initialize the largest prime factor variable
    largest_prime = 0
    # Start dividing by 2
    while number % 2 == 0:
        largest_prime = 2
        number = number // 2
    # Continue with odd numbers
    for i in range(3, int(number**0.5) + 1, 2):
        while number % i == 0:
            largest_prime = i
            number = number // i
    # If the remaining number is a prime greater than 2
    if number > 2:
        largest_prime = number
    return largest_prime

# Example usage
number = int(input("Enter a number: "))
print("Largest prime factor:", largest_prime_factor(number))