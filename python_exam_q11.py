# Write a function named christmas_tree which takes in an integer n representing
# the height of the christmas tree. The trunk always has a height of 2. Here are some
# examples:
def print_christmas_tree(n):
    for i in range(n):
        print(" "*(n-i-1)+"*"*(2*i+1))
    for i in range(2):
        print(" "*(n-1) + "*")

print_christmas_tree(3)