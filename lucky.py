def lucky_numbers(num_list):
    hash_map ={}
    for num in num_list:
        hash_map[num]=hash_map.get(num,0)+1
    lucky = [key for key in hash_map if hash_map[key] == key]
    if lucky:
        most = max(lucky)
        return max([key for key in lucky if hash_map[key]==most])
    else:
        return -1

print(lucky_numbers([1,2,2,2,1]))