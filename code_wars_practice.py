def word_pattern(pattern, string):

    listA = string.split(' ')
    new_dict = {}
    
    if len(pattern) != len(listA):
        return False
    
    for index, letter in enumerate(pattern):
        new_dict[letter] = new_dict.get(letter, listA[index])

    if len(new_dict.values()) != len(set(listA)):
        return False
        
    for index, item in enumerate(pattern):
        if new_dict[item] != listA[index]:
            return False
        
    return True
    
    