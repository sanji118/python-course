def sum_list(lst):
    if len(lst)==0:
        return 0
    else:
        return lst[0]+sum_list(lst[1:])
print(sum_list([3,4,5,78,90]))