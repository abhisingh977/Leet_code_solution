class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1=len(nums1)                   #length of nums1
        l2=len(nums2)                   #length of nums2
        i=0
        j=0
        a=[]                            # Create a empty list a

        while i<l1 and j<l2:
            if (nums1[i]<=nums2[j]) :       #comparing nums1 and nums2
                a.append(nums1[i])          #if nums1 is less than or equal to nums1 then add it to list a
                i=i+1                       # and increase the i index
            else:
                a.append(nums2[j])         # if nums2 is greater than nums2 then add it to list a 
                j=j+1                      # and increse the j index

        a = a + nums1[i:] + nums2[j:]     # add all the remaning value if the one of the list is complete  

        l3=len(a)                           # length of combined list
        div=l3/2    
        divone=int(div-1)
        if div==1:
            s=(a[(divone)]+a[int(div)])/2
        elif l3%2==0:
            s=(a[divone]+a[int(div)])/2    
        else:
            s=a[int(div)]
        return(s)

