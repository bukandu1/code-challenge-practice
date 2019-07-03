def word_pattern(pattern, string):

    listA = string.split(' ')
    new_dict = {}
    letter = 'a'
    
    for item in listA:
        new_dict[item] = new_dict.get(item, letter)
        if new_dict[item] == letter:
            letter = chr(ord(letter) + 1)
    
    for index, item in enumerate(listA):
        if new_dict[item] != pattern[index]:
            return False
            
    return True
    
    print(new_dict)

        
    