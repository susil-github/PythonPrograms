nums = [1,2,3,2,2,4,5]

dict = {}

for item in nums:
    if item not in dict:
        dict[item]=1
    else:
        dict[item]=dict[item]+1

max_num = max(dict.values())
max_freq_num = 0
for key, value in dict.items():
    if value == max_num:
        max_freq_num=key
        break

print(f'the max freuqency no is -> {max_freq_num}')