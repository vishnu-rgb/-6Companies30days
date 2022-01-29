class Solution:
    def maxProfit(self, K, N, A):
        # code here
        if K >= N - 1:
            profit = 0
            for i in range(1, N):
                if A[i] > A[i-1]:
                    profit += A[i] - A[i-1]
            return profit
        
        buys = [-float('inf') for _ in range(K+1)]
        sells = [0 for _ in range(K+1)]
        
        for p in A:
            for i in range(1, K+1):
                buys[i] = max(buys[i], sells[i-1] - p)
                sells[i] = max(sells[i], buys[i] + p)
        
        return sells[-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends