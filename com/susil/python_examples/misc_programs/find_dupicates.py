nums = [1,2,3,4,5,2,3,6]

new_list =[]
dup_list=[]

for item in nums:
    if item not in new_list:
        new_list.append(item)
    else:
        dup_list.append(item)

print(dup_list)
