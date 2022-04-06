#1-
class Person:
    
    def __init__(self,first_name,last_name):
        
        self.first_name = first_name
        self.last_name = last_name
        
    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
        
person = Person("okan","özTaN")
print(person)


#2- computes the distance between points in two dimensions

from ac import *
import math

class Point2D:
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        
    def calculate_distance(self,other):
        
        distancee = (self.x - other.x)**2 + (self.y - other.y)**2
        return math.sqrt(distancee)
    
point1 = Point2D(4, 7)
point2 = Point2D(5, 2)
distance = point1.calculate_distance(point2)
print(distance)

#3-
class Time:
    
    def __init__(self, hour, minute, second):
        """
        a Time instance giving the hour, minute and second.
        """
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def total_seconds(self):
        """
        the total number of seconds since the start of the day.
        """
        return 3600 * self.hour + 60 * self.minute + self.second
    
    def __str__(self):
        """
        a string representation of this time.
        """
        s = ''
        if self.hour < 10:
            s += '0'
        s += str(self.hour)
        s += ':'
        if self.minute < 10:
            s += '0'
        s += str(self.minute)
        s += ':'
        if self.second < 10:
            s += '0'
        s += str(self.second)
        return s

# Solution testing
my_time = Time(9, 5, 7)
my_seconds = my_time.total_seconds()
print(my_seconds)
print(my_time)


#4-
class FreqTable:
        
    def __init__(self):
        self.count = {}
    
    def add(self,element):
        # Check if this is the first time
        if element in self.count:
            self.count[element] += 1
            return self.count[element]
            
        else:
            self.count[element] = 1
            return self.count[element]
            
    def get_count(self,element):
        
        # Check if the element was ever added
        if element not in self.count:
            return 0
        return self.count[element]
    
    
freq_table = FreqTable()
for _ in range(3):
    freq_table.add(0)
print(freq_table.get_count(0))
print(freq_table.get_count(1))


#5- When a person joins to the back of queue, leave a person from front of the queue in a supermarket queue
class SupermarketQueue:
    
    def __init__(self):
        self.queue = []
        
    def add_to_back(self,name):
        self.queue.insert(0,name)
        return self.queue
    
    def remove_from_front(self):
        return self.queue.pop(-1)
        
    def __str__(self):
        return f"{self.queue}"
    
    def __len__(self):
        return len(self.queue)
        
# Solution testing
queue = SupermarketQueue()
queue.add_to_back('Alice')
queue.add_to_back('Bob')
print(len(queue))
print(queue)
print(queue.remove_from_front())



#6- User class
class User():
    
    def __init__(self, row):
        self.id      = row[0]
        self.email   = row[1]
        self.name    = row[2]
        self.address = row[3]

# Read the CSV and create User instances
users = []
import csv
with open('user_file.csv') as f:
    reader = csv.reader(f)
    rows = list(reader)
    for row in rows[1:]:
        user = User(row)
        users.append(user)

# Solution testing
last = users[-1]
print(last.id)
print(last.email)
print(last.name)
print(last.address)