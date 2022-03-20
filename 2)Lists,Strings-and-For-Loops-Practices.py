#1- print the poem
lines = ["My candle burns at both ends;", "It will not last the night;", 
         "But ah, my foes, and oh, my friends —", "It gives a lovely light."]

for line in lines:
    print(line)


#2- range built-in func
number = 9

for i in range(number):
    print(i)


#3- print between 50 and 77 (both inclusive)
for i in range(50,78):
    print(i)


#4- increase each value
values = [18, 3, 9, 2, 19, 12, 5, 22, 2, 10, 10, 17, 17, 14, 2, 16, 19, 7, 9, 19,78,64,7]

for i in range(len(values)):
    
    values[i] += 1
    
#5- reserved values in the list
values = [17, 1, 7, 2, 39, 12, 5, 21, 5, 10, 19, 14, 1, 9,50,63,87]
reversed_values = values[::-1]

#6- compute total list
values = [5, 3, 1, 9]

total = 0
for i in values:
    total += i
    
#7- copy the following list
values = [6, 2, 1, 8, 5, 3, 9, 7]
values_copy = []
for value in values:
    values_copy.append(value)
    
    
#8- 7 by 3 matrix where each number is equal to 1
matrix  = []

for i in range(7):
    matrix.append([])
    for j in range(3):
        matrix[i].append(1)
        
#9- calculate the number of the rows and columns       
matrix = [
    [0, 9, 5, 4, 5, 3, 1, 5, 7],
    [8, 2, 1, 7, 3, 1, 5, 7, 0],
    [1, 5, 3, 2, 7, 1, 4, 4, 8],
    [2, 5, 6, 2, 0, 4, 1, 9, 3],
    [7, 4, 2, 9, 7, 0, 7, 4, 4],
]
num_rows = len(matrix)
num_cols = []    

for i in range(len(matrix)):
    num_cols.append(len(matrix[i]))
    

#10- Write a Python program that sums all values in the matrix
matrix = [
    [0, 9, 5, 4],
    [8, 2, 3, 0],
    [1, 5, 3, 2]
]
total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        total += matrix[i][j]


#11- calculates the average the following list
values = [61, 20, 45, 63, 96, 71, 6, 8, 72, 22, 97, 7, 46, 11, 15, 74, 81, 69, 70, 26]
list_length = len(values)

total = 0
for value in values:
    total += value

average = total / list_length     


#12- calculate the length of the string elements in the list
words = ['tissue', 'psychology', 'blind', 'assessment', 'dynamic', 'hero', 'circulation',
         'seller', 'publication', 'interview', 'show', 'joy', 'sour', 'feature', 'grass', 
         'optimum', 'inplace', 'pressure', 'bullet', 'car']

word_len = []
for word in words:
    word_len.append(len(word))
    

#13- string to list then list to string
message = 'Hello, There'
print(type(message)) # str

message = message.split(',')
print(type(message)) #list

message = ''.join(message)
print(type(message)) #str 