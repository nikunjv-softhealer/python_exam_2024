def is_turn_good(X, Y):
    s = X + Y
    if s > 6:
        return "Yes"
    else:
        return "No"

result = is_turn_good(4,2)
print(result)