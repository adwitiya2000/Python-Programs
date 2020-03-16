#Given an integer,n, perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird

#Input Format
#    A single line containing a positive integer, .

#Constraints
#    1<=n<=100
#Output Format
 #   Print Weird if the number is weird; otherwise, print Not Weird.

#Sample Input 0  Sample Output 0
#3               Weird

#Explanation 0
 #   3 is odd and odd numbers are weird, so we print Weird.

#Sample Input 1  Sample Output 1
#24              Not Weird

#Explanation 1
#    24>20 and 24 is even, so it isn't weird. Thus, we print Not Weird.


#Ouput

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if (n%2==0):
    if(n>20):
        print('Not Weird')
    elif(n>6 & n<=20):
        print('Weird')
    elif(n>=2 & n<5):
        print('Not Weird')
else:
    print('Weird')
