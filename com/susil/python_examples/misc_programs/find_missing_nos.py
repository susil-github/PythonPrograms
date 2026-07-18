li = [1,2,3,5]

missing_no_list=[]
for item in li:
    if item+1 not in li and item != li[-1] :
        missing_no_list.append(item+1)
    else:
        pass
print(missing_no_list)
