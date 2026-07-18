nums = [1,2,2,3,4,1,5]

new_list = []

for item in nums:
    if item not in new_list:
        new_list.append(item)
    else:
        continue
print(nums)
print(new_list)