class Solution:
    def isPalindrome(self, x: int) -> bool:  # Is True or False
        i=0
        
        if(x<0 or x%10==0):
            
            if (x==0):
                return True
            return False
        else:
            while (x>i):
                a=int(x%10)
            
                i=int(x%10)+(i*10)
            
                x=int(x/10)
        if (x==i or x==int(i/10)):
            return(True)
        else:
            return(False)
            
        