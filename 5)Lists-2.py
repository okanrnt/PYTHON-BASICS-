#1- Write a function that returns the first five elements in a list 
def first_five(some_list):
    return some_list[:5]

#2- Write a function that returns the last five elements in a list
def last_five(list_):
    return list_[-5:]

#3- Write a function that starts with the second element of the list,that skip every two elements,
#does not keep any element whose index is greater than 11
def skip_two(skip_list):
    skip_two_list = []
    index = 1
    for element in elements:
        skip_two_list.append(elements[index])
        index += 3
        if index > 11:
            break
    return skip_two_list
#alternative
def skip_two(some_list):
    return some_list[1:11:3]

#4- Write a function, skip_one, that given a list, returns a list that skips every other element 
#and includes the first one
def skip_one(some_list):
    return some_list[::2]

#5- returns a list consisting of the multiples of 5
def mult_five(some_list):
    multiples = []
    for element in some_list:
        if element%5 == 0:
            multiples.append(element)
    return multiples
#alternative
def mult_five(some_list):
    return some_list[0::5]

#6- return reverse
def reverse(some_list):
    return some_list[::-1]

#7- combine two different lists
def concatenate(list1,list2):
    return list1 + list2

#8- write a function that return the count of any number
def count(some_list,number):
    count = 0
    for element in some_list:
        if element == number:
            count += 1
    return count
#alternative
def count(some_list,number):
    return some_list.count(number)

#9- Returns index of a first occurrence of the object in a list, if it's in it. Otherwise returns -1
def find_first(some_list,number):
    for element in some_list:
        if element == number:
            return some_list.index(element)
    return -1

#10- substract the index that is wanted
def remove_at_idx(some_list, idx):
    return some_list[:idx]+some_list[idx+1:]
#alternative
def alternative_remove(some_list,idx):
    some_list.pop(idx)
    return some_list

#11- insert a new element for index that is want into a list
def insert(some_list,letter,idx):
    some_list.insert(idx,letter)
    return some_list    
#solution 2
def insert(some_list, obj, idx):
    return some_list[:idx]+[obj]+some_list[idx:]

#12- remove a element for index that is want into a list
def remove_at_idx(some_list, idx):
    some_list.pop(idx)

#13- clear all any list 
def clear_stack(list_name):
    return list_name.clear()

#14- remove a element that is want 
def remove_first(some_list,number):
    some_list.remove(number)
    return some_list

#15- cocmbine two lists
def extend_list(list1,list2):
    list1.extend(list2)
    return list1

#16- sorts a list in descending order in place
def sort(some_list):
    some_list.sort(reverse=True)
    return some_list

#17- Takes as input a list where each element is a list with three elements.
# Orders it by index 2 in ascending order.
# Resolves ties by sorting by index 0, also in ascending order.
# Modifies the input in place.
def sort_index(some_list):
    some_list.sort(key=lambda x: (x[2], x[0]))
    return some_list

#18- Takes as input a list of lists
# Orders the outer list by the third element in the inner lists in descending order
# Resolves ties by sorting by the first one in ascending order
# Modifies the input in place
def sort_index(some_list):
    some_list.sort(key=lambda x : x[0])
    some_list.sort(key=lambda x : x[2],reverse=True)
    return some_list