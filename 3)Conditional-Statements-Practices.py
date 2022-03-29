#1- count how many numbers greater than 100 in a number list

count=0
for value in values:
    if value > 100:
        count +=1


#2- count how many even and odd numbers are in the values

num_even = 0
num_odd = 0
for value in values:
    if value % 2 == 0:
        num_even +=1
    else:
        num_odd +=1
        
#3- check whether list1 is the reverse of list2

is_reversed = list1 == list2[::-1]


#4- find the characters that are common to both string1 and string2 any senteces

common_letters = []
for s in string1:
    if (s in string2) and (s not in common_letters):
        common_letters.append(s)

#5- find the maximum value in a number list

maximum = values[0]

for value in values:
    if value > maximum:
        maximum = value


#6- find the minimum value in a number list

minimum = values[0]
for value in values:
    if value < minimum:
        minimum = value
        
        
#7- Find two distinct numbers in values whose sum is equal to 100 in a number list

value1 = None
value2 = None
for a in values:
    for b in values:
        if (a != b) and (a + b == 100):
                value1 = a
                value2 = b       

#8- find the number that appears the most in a number list
most_frequent = values[0]

for value in values:
    if values.count(value) > values.count(most_frequent):
        most_frequent = value