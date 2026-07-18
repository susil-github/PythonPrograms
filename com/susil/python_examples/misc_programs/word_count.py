'''
count the no of times each word
'''
li = ['mango', 'apple','mango','orange','apple','mango']

dict = {}

for item in li:
    if item not in dict:
        dict[item]=1
    else:
        dict[item] = dict[item]+1

print(dict)
print('now iterate to show again..')
for key, value in dict.items():
    print(key," ", value)
