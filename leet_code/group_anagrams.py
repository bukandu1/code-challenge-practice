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