import sys
class Solution:
    ans = ''
    name = 'A'
    def returnString(self, i, j, n, bracket):
        if (i==j):
            self.ans = self.ans+self.name
            self.name = chr(ord(self.name) + 1)
            return
        
        self.ans = self.ans + "("
        self.returnString(i, bracket[i][j], n, bracket)
        self.returnString(bracket[i][j]+1, j, n, bracket)
        self.ans = self.ans + ")"
    
    def matrixChainOrder(self, p, n):
        # code here
        m = [[0 for x in range(n)] for x in range(n)]
        b = [[0 for x in range(n)] for x in range(n)]
        
        for l in range(2, n):
            for i in range(1, n-l+1):
                j = i+l-1
                m[i][j] = sys.maxsize
                for k in range(i, j):
                    q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                    if q < m[i][j]:
                        m[i][j] = q
                        b[i][j] = k
        self.returnString(1, n-1, n, b)
        return self.ans
