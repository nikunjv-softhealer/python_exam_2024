def max_people_traveling(N, M):
    max_people = 0
    
    for num_5_seaters in range(N + 1):
        for num_7_seaters in range(M + 1):
            total_people = num_5_seaters * 5 + num_7_seaters * 7
            if total_people > max_people:
                max_people = total_people
                
    return max_people

result = max_people_traveling(5, 7)

print(result)