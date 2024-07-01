# 9) Write a Python program to create a new dictionary by extracting the mentioned
# keys from the dictionary below.
sample_dict = {
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
}

key = ["name", "salary"]

new_dict = dict()

for i, j in sample_dict.items():
    if i in key:
        new_dict.update({i:j})
print(new_dict)
