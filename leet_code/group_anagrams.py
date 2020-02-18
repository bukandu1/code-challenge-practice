"""
Given an array of strings, group anagrams together.

Example: 
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output:
[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]
"""

class Solution:
    def group_anagrams(self, words_list):
        # create dictionary to store strings to group anagrams
        # loop words list:
            # sort word and check if in dictionary
            # if in dictionary: add to list
            # else: create new key and add word to new list

        # add results to result list by looping through keys

        word_dict = {}
        for word in words_list:
            sorted_word = ''.join(sorted(word))
            print(sorted_word)
            if sorted_word not in word_dict:
                word_dict[sorted_word] = [word]
            else:
                word_dict[sorted_word].append(word)
        # print(word_dict)

        return [word_dict[key] for key in word_dict]

s = Solution()

# TEST
s.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
s.group_anagrams([]))
