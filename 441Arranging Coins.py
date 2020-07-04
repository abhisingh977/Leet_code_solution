class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1 or n==0:
            return(n)
        c=0       
        for i in range(1,n+1):
            c+=i
            if c>n:
                return(i-1)
                         

    
    
    
    
    
    
