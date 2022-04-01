#1- swap the keys with the values
def swap(some_dict):
    return {value : key for key,value in some_dict.items()}

#2- returns the value for that key if the key is in the dictionary, otherwise returns the given object
def default(some_dict,p_key,obj):
    if p_key in some_dict:
        return some_dict[p_key]
    else:
        return obj
    
    
#3- If the key isn't in the dictionary, sets they key to the given object
def default_add(some_dict,key,obj):
    if key in some_dict:
        return some_dict[key]
    else:
        some_dict[key] = obj
        return obj


#4- updates the given dictionary with the values in the iterable if the key is in the dictionary. 
#If the key isn't in the dictionary, adds it with the value in the iterable(like tuples in a list)
def update(a_dict,iterable):
    a_dict.update(iterable)
    return a_dict


#5- it removes that key from the dictionary and returns the corresponding value. 
#If the key isn't in the dictionary, it returns None
def remove(some_dict,key):
    if key in some_dict:
        value = some_dict[key]
        some_dict.pop(key)
        return value
    else:
        return None

#6- {column_name: {index: value}}, and a list of rows, returns a new dictionary without the given rows
def remove_rows(some_dict,keys_to_remove):
    for col in some_dict:
        for key in keys_to_remove:
            some_dict[col].pop(key)
    return some_dict

for column,values in remove_rows(d, [index1, index2]).items():
    print(column, values, sep="\n")
    
#7- {column_name: {index: value}} and a column name,
#returns a new dictionary where they keys are the values in the given column name, 
#and the values are the averages of total_bill, tip and size in this order, for each value
d = {
    'total_bill': {69: 15.01, 103: 22.42, 84: 15.98, 207: 38.73, 0: 16.99},
    'tip': {69: 2.09, 103: 3.48, 84: 2.03, 207: 3.0, 0: 1.01},
    'sex': {69: 'Male', 103: 'Female', 84: 'Male', 207: 'Male', 0: 'Female'},
    'smoker': {69: 'Yes', 103: 'Yes', 84: 'No', 207: 'Yes', 0: 'No'},
    'day': {69: 'Sat', 103: 'Sat', 84: 'Thur', 207: 'Sat', 0: 'Sun'},
    'time': {69: 'Dinner', 103: 'Dinner',
             84: 'Lunch', 207: 'Dinner', 0: 'Dinner'},
    'size': {69: 2, 103: 2, 84: 2, 207: 4, 0: 2}
}

def avg_group(some_dict,column_name):
    male_index = []
    female_index = []
    male_values = []
    female_values = []
    avg_male = []
    avg_female = []
    for keys,values in some_dict.items():
        if keys == column_name:
            for index,value in some_dict[keys].items():
                if value == "Male":
                    male_index.append(index)
                elif value == "Female":
                    female_index.append(index)
                else:
                    pass
            for keys,values in some_dict.items():
                if keys == "total_bill":
                    for m_index in male_index:
                        if m_index in some_dict[keys]:
                            male_values.append(some_dict[keys][m_index])
                    avg = sum(male_values) / len(male_index)
                    avg_male.append(avg)
                    male_values.clear()
                    
                    
                    for f_index in female_index:
                        if f_index in female_index:
                            female_values.append(some_dict[keys][f_index])
                    avg = sum(female_values) / len(female_index)
                    avg_female.append(avg)
                    female_values.clear()
                    
                    
            for keys,values in some_dict.items():
                if keys == "tip":
                    for m_index in male_index:
                        if m_index in some_dict[keys]:
                            male_values.append(some_dict[keys][m_index])
                    avg = sum(male_values) / len(male_index)
                    avg_male.append(avg)
                    male_values.clear()
                    
                    
                    for f_index in female_index:
                        if f_index in female_index:
                            female_values.append(some_dict[keys][f_index])
                    avg = sum(female_values) / len(female_index)
                    avg_female.append(avg)
                    female_values.clear()
                    
            
            for keys,values in some_dict.items():
                if keys == "size":
                    for m_index in male_index:
                        if m_index in some_dict[keys]:
                            male_values.append(some_dict[keys][m_index])
                    avg = sum(male_values) / len(male_index)
                    avg_male.append(avg)
                    male_values.clear()
       
                    
                    for f_index in female_index:
                        if f_index in female_index:
                            female_values.append(some_dict[keys][f_index])
                    avg = sum(female_values) / len(female_index)
                    avg_female.append(avg)
                    female_values.clear()
                    
    return {"Female":avg_female,"Male":avg_male}

#alternative
def get_avgs(d, value, indices):
    sums = [0 for _ in range(3)]
    for idx in indices:
        sums[0] += d["total_bill"][idx]
        sums[1] += d["tip"][idx]
        sums[2] += d["size"][idx]
    return list(map(lambda x: x/len(indices), sums))

def avg_group(d, col):
    data = d[col]
    groups = list(set(d[col].values()))
    groups.sort()
    
    group_by = {}
    
    for key in groups:
        indices = [k for k,v in d[col].items() if v == key]
        group_by[key] = get_avgs(d, key, indices)
            
    return group_by