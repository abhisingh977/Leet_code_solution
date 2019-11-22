class Solution:
    def isValid(self, s: str) -> bool:
        
    
        dict1={"{":"}","[":"]","(":")"}         #Create a dict

        stack=[]                                # Create a empty a stack 
        for i in range(len(s)):
            if s[i] in dict1.keys():            
                stack.append(s[i])              # Append the value in Stack if they are opening bracket
            else:
                if len(stack)==0:               
                    return False                # If the Stack empty and we have a close bracket then return                                                   #false
                p=stack.pop()                   
                if s[i]!=dict1[p]:              # if the closing bracket is not paired with the last element of                                                 #the stack then return false
                    return False
        if len(stack)==0:                      # Check if the stack is empty or not if it's empty 
            
            return True
        else:
            return False                       # If stack is not empty then return False.
  
