def max_num_in_list( list ):
    max = list[ 0 ]
    for a in range(len(list)):
        if list[a] > max:
            max = list[a]
    return max
print(max_num_in_list([1, 2, -8, 0]))