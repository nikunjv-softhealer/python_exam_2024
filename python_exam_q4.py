# 4) Write a program to create function calculation() such that it can accept two
# variables and calculate addition and subtraction. Also, it must return both addition
# and subtraction in a single return call.

def my_function(num1, num2):
    addition = num1 + num2
    subtraction = num1 * num2
    calculation = {'addition':addition, 'subtraction':subtraction}
    if addition and subtraction:
        return calculation
        
fun = my_function(500,10)
print(fun)
