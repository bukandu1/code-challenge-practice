def word_pattern(pattern, string):

    listA = string.split(' ')
    new_dict = {}
    
    if len(pattern) != len(listA):
        return False
    
    for index, letter in enumerate(pattern):
        new_dict[letter] = new_dict.get(letter, listA[index])
    print(new_dict)
    print(pattern)
    print(string)

    for index, item in enumerate(pattern):
        print('dictionary item: {0} and current pattern: {1}'.format(new_dict[item],pattern[index]))
        if new_dict[item] != listA[index]:
            return False
            
    return True