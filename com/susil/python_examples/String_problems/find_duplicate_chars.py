from collections import Counter

s = "programming"
count = Counter(s)

word_list =[]
for key, value in count.items():
    if value >1:
        word_list.append(key)

print('duplicate chars are:',word_list)