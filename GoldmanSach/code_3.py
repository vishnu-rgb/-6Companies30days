# Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product less than a given number k.

# Example 1:

# Input : 
# n = 4, k = 10
# a[] = {1, 2, 3, 4}
# Output : 
# 7
# Explanation:
# The contiguous subarrays are {1}, {2}, {3}, {4} 
# {1, 2}, {1, 2, 3} and {2, 3} whose count is 7.

class Solution:
    def countSubArrayProductLessThanK(self, A, n, k):
        #Code here
        if k == 0: 
            return 0

        count, curr, start = 0, 1, 0

        for i in range(len(A)):
            curr *= A[i]
            while start < i and curr >= k:
                curr //= A[start]
                start += 1            
            if curr < k: 
                count += (i-start) + 1

        return count