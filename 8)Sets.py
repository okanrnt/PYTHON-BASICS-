# write a function, unique, that takes a list as input and returns it without duplicated elements.
def unique(some_list):
    for_unique = set()
    for element in some_list:
        for_unique.add(element)
    return list(for_unique)

#solution 2
def unique(some_list):
    return list(set(some_list))

# Returns the boolean value True if the lists have the same input, and False otherwise
def same_elements(list1,list2):
    if sorted(list1) == sorted(list(set(list2))):
        return True
    else:
        return False
    
    
#solution 2
def same_elements(list1, list2):
    return set(list1) == set(list2)

# Returns the boolean value: True if all the elements of the first argument are in the second one. False otherwise
False otherwise
def subseteq(iter1,iter2):
    union_set = set(iter1).union(set(iter2))
    return union_set == set(iter2)

#solution 2
def subseteq(iter1, iter2):
    return set(iter1).issubset(iter2)

# True if both of these conditions are met: All the elements of the first argument are in the second one. 
#There's an element in the second argument not present in the first one. False otherwise
def subset(iter1,iter2):
    return set(iter1).issubset(iter2) and len(set(iter1)) != len(set(iter2))
    
# solution 2
def subset(iter1, iter2):
    return set(iter1) < set(iter2)

# Returns the boolean value: True if no elements belong to both iterables. False otherwise
def disjoint(iter1,iter2):
    return set(iter1).isdisjoint(iter2)


# Returns a set with the elements that are in both iterables
def intersect(iter1,iter2):
    return set(iter1).intersection(iter2)

# Returns a set with the elements that are in either of the iterables
def union(iter1,iter2):
    return set(iter1).union(iter2)


# Returns a set with the elements of the first iterable that aren't in the second one.

def difference(iter1,iter2):
    return set(iter1).difference(iter2)

# Returns a set with the elements that either: Are in the first iterable, but not in the second, 
#or Are in the second iterable, but not in the first

def sym_diff(iter1,iter2):
    return set(iter1).symmetric_difference(iter2)


# returns the sets A∖B, B∖A and A∩B
def part(set1,set2):
    
    dif1 = set1.difference(set2)
    dif2 = set2.difference(set1)
    inter_sec = set1.intersection(set2)
    
    return dif1,dif2,inter_sec


#The number of elements in their union.
#The number of elements in the first one.
#The number of elements in the second one.
#The number of elements in both of them.

def iep(set1,set2):
    union = set1.union(set2)
    inter_sec = set1.intersection(set2)
    return len(union), len(set1), len(set2), len(inter_sec)