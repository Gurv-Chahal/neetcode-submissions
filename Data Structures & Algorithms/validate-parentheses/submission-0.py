class Solution:

    # O(N) time and O(N) space
    def isValid(self, s: str) -> bool:
        
        brackets = []

        # iterate over input array
        for i in range(len(s)):
            
            # if index is a front bracket, append it
            if s[i] in '([{':
                brackets.append(s[i])
            
            # if index is closing bracket
            elif s[i] in ')]}':
                # case 1: array is empty, if it is return false
                if len(brackets) == 0:
                    return False
                
                # case 2: '('
                if s[i] == ')' and brackets[-1] != '(':
                    return False
                # case 3: '['
                elif s[i] == ']' and brackets[-1] != '[':
                    return False
                # case 4: '{'
                elif s[i] == '}' and brackets[-1] != '{':
                    return False
                # if the brackets match then we pop the opening bracket off the stack
                # this is because if we have an empty stack at the end it means we found all
                # the matches
                else:
                    brackets.pop()
        
        # if condition is true then its True
        return len(brackets) == 0
                
