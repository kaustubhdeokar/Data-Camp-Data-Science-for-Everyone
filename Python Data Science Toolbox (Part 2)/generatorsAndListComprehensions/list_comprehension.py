nums = [1,2,3,4]
nums = [num+1 for num in nums]

#double loop list comprehensions
pairs = [(num1,num2) for num1 in range(0,2) for num2 in range(6,10)]

#matrix creation
matrix = [[i for i in range(0,5)] for j in range(0,5)]

list1 =  [num**2 for num in range(10) if num%2==0]
list2 = [num**2 if num%2==0 else 0 for num in range(10)]

dictionary_comprehensions = {num:-num for i in range(10)}
