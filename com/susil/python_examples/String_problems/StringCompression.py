from collections import Counter
str = 'aaabbcc'
count = Counter(str)
new_str = ''
for key, value in count.items():
    new_str = new_str + key+ value.__str__()

print(new_str)

