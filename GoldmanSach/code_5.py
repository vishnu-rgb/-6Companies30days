# Ugly Number 
# link: https://practice.geeksforgeeks.org/problems/ugly-numbers2254/1/

class Solution:
	def getNthUglyNo(self,n):
	    arr = [0]*n             # a list containing 0 and of size n
        arr[0] = 1              #  first element of list would be 1 always 
        x2 = x3 = x5 = 0        # will tell us about the index of 2, 3, 5

        mul2 = 2                # initial multipl of 2 is 2 
        mul3 = 3                # initial multipl of 3 is 3 
        mul5 = 5                # initial multipl of 5 is 5 

        for i in range(1,n):
            arr[i] = min(mul2, mul3, mul5)               # checking minimum here after taking initial values it will be 2 from (2, 3, 5)
                                                         # now we have arr[1] = 2 so arr = [1, 2, 0, 0, 0, ........ ] and i = 2 now 
            if arr[i] == mul2:                           # now i is 2 and arr[2] is equal to multiple of 2 which is 2 as we defined
                x2+=1                                    # x2 will increse by 1 and x2 = 1 now 
                mul2 = arr[x2] * 2                       # multiple of 2 will be = arr[x2] * 2 = 2 * 2 = 4 | 
            if arr[i] == mul3:                           # now mul2 = 4 and mul3 = 3 and mul5 = 5 | find min as in line 11
                x3+=1                                    # a[3] will now be = 3 | arr = [1, 2, 3, 0, 0, .....]
                mul3 = arr[x3] * 3                       # again same process follows 
            if arr[i] == mul5:
                x5+=1
                mul5 = arr[x5] * 5
        return arr[-1]
