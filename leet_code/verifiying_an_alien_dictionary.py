class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        
        guaruntee that 
        test cases:
        - all word in order, different first letters
        - words not in order, diff 1st letters
        - some words start with same letter
        - no words
        
        if len(words) ==  0 or 1:
            return True
        
        loop words list until len(words) - 1
        
            if the current word and the next word have the same letter:
                compare each letter until determine different letters
                save those letters 
                
            if differnt letters:
                determine the index of the current word  
                determine index  of the next word
                
                if the current index > next index:
                    return False
        
        return True
                
        complexity: O(n)
        
        """

        if len(words) == 0 or len(words) == 1:
            return True

        for i in range(0, len(words) - 1):
            current_index = 0
            current_word = words[i]
            next_word = words[i+1]

            while current_word[current_index] == next_word[current_index] and current_index < len(current_word) - 1 and current_index < len(next_word) - 1:
                current_index += 1

            current_word_index = order.find(current_word[current_index])
            next_word_index = order.find(next_word[current_index])

            if current_word_index >= next_word_index:
                return False

        return True
