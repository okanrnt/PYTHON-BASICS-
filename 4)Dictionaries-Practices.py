#1- change 'age' from current value to new value.

some_dict[current_value] = new_value

#2- take all the keys in a dictionary

keys = []
for key in some_dict.keys():
    keys.append(key)
    
#3- take all the values in a dictionary

values = []
for value in some_dict.values():
    values.append(value)

#4- combine the keys and values lists as a dict

my_dict = {}
for key,value in zip(keys_list,values_list):
    my_dict[key] = value

#5- replace ", to ." and "uppercase to lowercase" and "space to underscore"
cleaning_dict = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 
                 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 
                 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 
                 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 
                 'Y': 'y', 'Z': 'z', ' ': '_', ',': '.'}

text_to_clean = "The claAs temPeraTUre is 17,8 deGrEes ceLSIus buT oUtsiDE It IS 25.4 degreeS"

cleaned_text = ""
for cur in text_to_clean:
    if cur in cleaning_dict:
        cleaned_text += cleaning_dict[cur]
    else:
        cleaned_text += cur