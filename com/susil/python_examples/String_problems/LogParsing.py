
count = 0
with open('sample.txt','r') as f:
    for line in f:
        #print(line)
        if 'ERROR' in line:
            count= count+1

print('the error count is :',count)