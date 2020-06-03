import re


file = open('withVivek.txt', encoding='utf-8')
file.readline()
newfile = open('cleaned_vivek.txt','w', encoding='utf-8')
raw = []
count=0
for index, line in enumerate(file.readlines()):
    x = re.search(r'(.+), (\d+:\d+) - (\w+): (.*)',line)
    if x == None:
##        print(index, line)
        count+=1
        raw[index-count][-1]+= line.strip()
    else:
        raw.append([*x.groups()])
##    if index==10: break

##print(raw[140:170])
for line in raw:
    newfile.write(','.join(line)+'\n')

file.close()
newfile.close()
