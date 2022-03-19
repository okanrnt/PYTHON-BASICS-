#1- Grade Point Average (GPA)
# grade * hours
multply_grade_hours = 5*4 + 3*2 + 4*3 + 2*2 + 3*3
total_hours = 4 + 2 + 3 + 2 + 3
gpa = multply_grade_hours / total_hours


#2- Write string of length 33 that contains 33 times the character *
stars = 33 * "*"


#3- convert from the seconds to hour and minute
seconds = 48600
hour = seconds // 3600
minute = (seconds - 3600 * hour) // 60


# 4- Find the body mass index
#name = weight(in kg) * height(in meters)
kemal = 67 / 1.82**2
okan = 68 / 1.78**2
cem = 50  / 1.55**2


#5- Compute the decimal part of x
x = 33.23423
decimal = x - int(x)



#6- You want to give the same number of apples to each person, but you don't want to bother cutting any apples
number_of_apples = 12333
numbers_of_persons = 3436

apples_ratio = number_of_apples / numbers_of_persons
apples_given_to_each = int(apples_ratio)
apples_left = (apples_ratio - apples_given_to_each) * numbers_of_persons


#7- The right answer
x = 2
y = 1
x = y
y = x

answer1 = 'x = 1 and y = 2'
answer2 = 'x = 1 and y = 1'
answer3 = 'x = 2 and y = 1'
answer4 = 'x = 2 and y = 2'

correct = answer2

#8- The right answer
x = 2
y = 1
tmp = x
x = y
y = tmp

answer1 = 'x = 1 and y = 2'
answer2 = 'x = 1 and y = 1'
answer3 = 'x = 2 and y = 1'
answer4 = 'x = 2 and y = 2'

correct = answer1

#9- convert the data types
tuplee = (12,44)
print(type(tuplee)) #tuple

listt = list(tuplee) 
print(type(listt)) #list

print(type(listt) == list) # True

print(type(type(listt) == list)) #bool

listtt = ["Turkey","Eskisehir"]
string = ','.join(listtt)
print(type(string)) #str