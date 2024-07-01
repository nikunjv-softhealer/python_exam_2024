# 5) Write a program to create a recursive function to calculate the sum of numbers
# from 0 to n, where n is user input.

def my_function(item):
    result = 0
    i = item
    while i > 0:
        result+=i
        i-=1
    print(result)

my_function(50)