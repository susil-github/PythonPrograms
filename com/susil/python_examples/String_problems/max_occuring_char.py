from collections import Counter

s = "dataengineering"

count = Counter(s)
print(count)
max_no = max(count.values())

for key,value in count.items():
    if value == max_no:
        print(key, end=', ')

    else:
        pass
