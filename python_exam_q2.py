# 2) sort a list of dictionaries by a value(age) of the dictionary
# —--------------------------------------
list = [
    {'name': 'Homer', 'age': 39},
    {'name': 'Bart', 'age': 10},
    {'name': 'Ketan', 'age': 5},
    {'name': 'Sagar', 'age': 50}
]

new_list = sorted(list,key = lambda x:x['age'])

for people in new_list:
    print(people)


