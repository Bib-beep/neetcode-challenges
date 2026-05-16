
class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []

        for c in s:
            if c == "{" or c == "(" or c =="[":
                myStack.append(c)
            elif c == "}" or c == ")" or c == "]":
                # Check top of stack to identify  if you've got opening bracket
                if len(myStack) == 0 : 
                    return False 
                else:  
                    topStack = myStack.pop()
                    if topStack == "{" and c == "}":
                        continue
                    elif topStack == "(" and c == ")":
                        continue
                    elif topStack == "[" and c== "]":
                        continue
                    else:
                        return False
        
        if myStack:
            return False
        else: 
            return True
                