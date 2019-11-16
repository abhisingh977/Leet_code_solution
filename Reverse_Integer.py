class Solution:
    def reverse(self, x: int) -> int:
        def rev(a):
            i=0
            while(a!=0):
                i=(a%10)+i
                i=i*10
                a=int(a/10)
            i=int(i/10)
            
            if ( i >= (2**31)-1 or i <=-2**31 ) :
                return 0
            else:
                return(i)

        
        
        
        if (x<0):
            x=abs(x)
            return(-rev(x))

        else:
            return(rev(x))


