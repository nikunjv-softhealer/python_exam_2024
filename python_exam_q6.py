# 6) Below are the two lists. Write a Python program to convert them into a dictionary
# in a way that item from list1 is the key and item from list2 is the value
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))
print(new_dict)