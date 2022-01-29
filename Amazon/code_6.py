class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        #code here
        deq, result = deque(), []
        for i in range(n):
            if i >= k:
                result.append(arr[deq[0]])
                if deq[0] < i - k + 1:
                    deq.popleft()
            while deq and arr[i] > arr[deq[-1]]:
                deq.pop()
            deq.append(i)
        
        result.append(arr[deq[0]])
        return result