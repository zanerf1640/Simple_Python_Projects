"""
This is a simple python script that inverts a list of numbers ranging 
from 0 to n-1, where n is provided by the user.

List Inversion Logic:
[ Head ,......, Tail ]  -->  [ Tail ,......, Head ]

Author: Zane Francis
"""


list = []

n = int(input("Enter number of elements in the list: "))

for i in range(0, n):
    list.append(i)

print("Original List: ", list)

# Inverting the list (comments explain the logic with n=20)
for i in range(0, n // 2): # when n is 20, the range goes from 0 to 9
    temp = list[i] # temp will hold the first element of list when i=0
    list[i] = list[n - i - 1] # If n=20, when i=0, list[19] is assigned to list[0]
    list[n - i - 1] = temp # list[0] is assigned to list[19]

print("Inverted List: ", list)
