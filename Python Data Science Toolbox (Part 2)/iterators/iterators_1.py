
#iter()

data = iter('Data')
try:
    while(1):
        print(next(data))
except:
    print('stop')

#iterating at once with *

data = iter('At once')
print(*data)

#iterating on a dictionary
data_dic = {'a':1,'b':2,'c':3}
for key,value in data_dic.items():
    print(str(key) +' has a value '+ str(value))

#iterating on a file.
file = open('filetoiterate','r')
file_iterator = iter(file)
try:
    while(1):
        print(next(file_iterator),end='')
except:
    print('eof')
