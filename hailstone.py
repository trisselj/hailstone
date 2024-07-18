# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/17/2024
# Description: Returns number of steps to take requested number to 1 in hailstone sequence

#Defining our function for this process (Assuming input is as expected)
def hailstone(n): #n = initial number of sequence
    steps = 0 #Return value being set to 0
    while n != 1: #Continues loop till n is 1
        if n % 2 == 0: #If the remainder after divided by two is zero then proceed
            n = n // 2 #Divides n by 2
        else: #For odd numbers
            n = 3 * n + 1 #Multiply by 3 and add 1
        steps += 1 #For every loop add 1 to steps
    return steps #Once complete return with the number of steps taken