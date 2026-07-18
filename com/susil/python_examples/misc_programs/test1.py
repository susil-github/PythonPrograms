str = '1011011101111101111'

l = []
item_list = []

for i in range(0,len(str)-1):
    if str[i] == '1':
        l.append(str[i])

    else:
        item_list.append(len(l))
        l.clear()
        continue

print(item_list)
print(max(item_list))
