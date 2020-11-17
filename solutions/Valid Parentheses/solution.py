    def isValid(self, s: str) -> bool:
        
        
        stack = []
        for char in s:
            if char =='(' or char =='{' or char =='[':
                stack.append(char)
            elif(len(stack) == 0):
                return False
            else:
                if  (char ==')' and not stack.pop() == '('):
                    return False
                elif  (char =='}' and not stack.pop() == '{'):
                    return False
                elif  (char ==']' and not stack.pop() == '['):
                    return False
        if(len(stack)==0):
            return True
        return False