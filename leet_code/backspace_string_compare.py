class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #create a stack for both strings
        # add each letter to stack if next letter is '#', pop stack
        # compare stack and return True if equal

        def resultString(string):
            stack = []
            for letter in string:
                if letter != '#':
                    stack.append(letter)
                else:
                    if not stack:
                        continue
                    else:
                        stack.pop()
            return "".join(stack)
    
        return resultString(S) == resultString(T)
        