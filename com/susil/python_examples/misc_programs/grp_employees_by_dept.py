employees = [
 ("John","IT"),
 ("Tom","HR"),
 ("Alice","IT"),
 ("Bob","Finance")
]

emp_dict ={}
emp_list=[]

for item in employees:
    if item[1] not in emp_dict:
        emp_dict[item[1]]=item[0]
    else:
        emp_list.append(emp_dict[item[1]])
        emp_list.append(item[0])
        emp_dict[item[1]]=emp_list

print(emp_dict)