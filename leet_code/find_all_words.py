import copy


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        #create two dictionaries (one - main, one -copy that will be manipulated)
        count = 0
        length = 0
        main_word_dict = dict()
        word_dict = dict()

        for char in chars:
            main_word_dict[char] = main_word_dict.get(char, 0) + 1
            word_dict[char] = word_dict.get(char, 0) + 1

        print(main_word_dict)
        #loop words list
        for word in words:

            count = 0
            for char in word:
                #check if each character is in dictionary (update by removing letter from dictionary)
                if char in word_dict:
                    if word_dict.get(char) > 0:
                        word_dict[char] = word_dict.get(char, 0) - 1
                        count += 1
                    elif word_dict.get(char) <= 0:
                        print("not in dict!")
                        count = 0
                        break
                else:
                    count = 0
                    break
            #print("adding", word, count)
            length += count
            word_dict = copy.deepcopy(main_word_dict)
            #print(word_dict)

        #if all letters found add length of words to count
        return length

# TODO: Write unittest