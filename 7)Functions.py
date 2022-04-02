#1
x = []
def f():
    x = []
    x.append(1)
    x.append(2)
    x.append(3)
    return x

f()
print(x)  #[]

#2
x = []
def f():
    x = []
    x.append(1)
    x.append(2)
    x.append(3)

f()
print(x) #[]

#3
x = []
def f():
    x = []
    x.append(1)
    x.append(2)
    x.append(3)

x = f()
print(x) #None

#4
x = []
def f():
    x.append(1)
    x.append(2)
    x.append(3)

f()
print(x) #[1,2,3]

#5
x = []
def f():
    x = []
    x.append(1)
    x.append(2)
    x.append(3)
    return x
​
x = f()
print(x) #[1,2,3]

#6- Write a function with two arguments to change to format time
def format_time(hour,minute):
    
    time = ""
    if hour < 10:
        time += "0"
    time += str(hour)
    time += ":"
    if minute < 10:
        time += "0"
    time += str(minute)
    return time


#7- Write a function named is_palindrome with one argument
def is_palindrome(dna):
    if dna == dna[::-1]:
        return True
    return False

#alternative
def is_palindrome(dna):
    n = len(dna)
    for i in range(n // 2):
        if dna[i] != dna[n - i - 1]:
            return False
    return True


#8- give the same number of apples to each person and do not cut any apples
def divide_apples(num_apples,num_people):
    per_person_apples = num_apples // num_people
    remaning_apples = num_apples % num_people
    return per_person_apples, remaning_apples

#9- return as hour,minute,second the seconds 
def seconds_to_hour_minute(num_seconds):
    hour = num_seconds // 3600
    minute = (num_seconds - hour * 3600) // 60
    remaining_second = num_seconds - (hour * 3600 + minute * 60)   
    return (hour, minute, remaining_second)

#10- if do_max is True, it returns max value. Otherwise False
def max_or_min(x,y,do_max=True):
    if do_max:
        return max(x,y)
    return min(x,y)

#11- find the frequency of the least frequent and the most frequent in a list
def most_least_frequent(values):
    frequencies = {}
    for value in values:
        if value not in frequencies.keys():
            frequencies[value] = 1
        else:
            frequencies[value] += 1
    max_freq = None
    min_freq = None
    for v in frequencies:
        if max_freq is None or frequencies[v] > max_freq:
            max_freq = frequencies[v]
        if min_freq is None or frequencies[v] < min_freq:
            min_freq = frequencies[v]
    return max_freq, min_freq

#12-
def most_least_frequent_all(values):
    frequencies = {}
    for value in values:
        if value not in frequencies:
            frequencies[value] = 1
        else:
            frequencies[value] += 1
    least = None
    most = None
    most_list = []
    least_list = []
    
    for freq in frequencies:
        #The frequency of the most frequent element
        if most is None or frequencies[freq] > most:
            most = frequencies[freq]
        #The frequency of the least frequent element
        if least is None or frequencies[freq] < least:
            least = frequencies[freq]
    
    for freq in frequencies:
        #The list of all elements with the maximum frequency
        if frequencies[freq] == most:
            most_list.append(freq)
        #The list of all values with the minimum frequency
        if frequencies[freq] == least:
            least_list.append(freq)
    return most_list,most,least_list,least