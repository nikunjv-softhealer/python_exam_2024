# 10) Delete a list of keys from a dictionary
sample_dict = {
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
}

key = ["name", "salary"]
new_dict = { i:j for i ,j in sample_dict.items() if i not in key}
print(new_dict)