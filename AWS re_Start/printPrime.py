'''
Display all the prime numbers between 1 to 250.
'''

for num in range(1, 251):  # Iterate through numbers from 1 to 250
    if num > 1:  # Check if the number is greater than 1
        for i in range(2, num):  # Iterate from 2 to the number
            if (num % i) == 0:  # Check if the number is divisible by any other number
                break  # If it is, break the loop
        else:
            print(num)