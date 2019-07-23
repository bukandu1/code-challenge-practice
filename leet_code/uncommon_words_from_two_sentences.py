
# We are given two sentences A and B.  (A sentence is a string of space separated words.  
# Each word consists only of lowercase letters.)

# A word is uncommon if it appears exactly once in one of the sentences, and 
# does not appear in the other sentence.

# Return a list of all uncommon words. 

# You may return the list in any order.
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
    #loop both strings and add to dictionary
    #loop dictionary and add only keys with value of 1 to list
    #return list
    
        word_dict = {}
        unique_list = []
        if not A or not B:
            if not A:
                return B.split(" ")
            elif not B:
                return A.split(" ")
            else:
                return unique_list
            
        for letter in A.split(" ") + B.split(" "):
            word_dict[letter] = word_dict.get(letter, 0) + 1
        print(word_dict)
        
        for key in word_dict:
            if word_dict[key] == 1:
                unique_list.append(key)
        
        return unique_list


# Runtime: 32 ms, faster than 93.00% of Python3 online submissions for Uncommon Words from Two Sentences.
# Memory Usage: 14 MB, less than 5.30% of Python3 online submissions for Uncommon Words from Two Sentences.