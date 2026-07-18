employees = [
    ("John", 50000),
    ("Alice", 70000),
    ("Bob", 60000),
    ("Tom", 90000),
    ("David", 80000)
]

item_list=[]
for item in employees:
    item_list.append(item[1])

item_list.sort()
item_list.reverse()
item_list= item_list[0:3]
print(item_list)

result_list = []
for item in item_list:
    for key in employees:
        if item in key:
            result_list.append(key)
        else:
            continue

print(result_list)



