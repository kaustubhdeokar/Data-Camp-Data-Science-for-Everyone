numbers = [chr(i+97) for i in range(10)]
enumerate_numbers = enumerate(numbers)


e_list = list(enumerate_numbers)

for index,value in enumerate(numbers):
    print(index,value)


for index,value in enumerate(numbers,start=5):
    print(index,value)

l1 = [i for i in range(10)]
l2 = [chr(i+97) for i in range(10)]

for one,two in zip(l1,l2):
    print(str(one)+":"+str(two))

z=zip(l1,l2)
print(*z)
