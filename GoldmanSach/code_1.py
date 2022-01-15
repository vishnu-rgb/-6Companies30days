class Solution:
    def Anagrams(self, words, n):
        def returnSorted(s):
            l = list(s)
            l.sort()
            return str(l)
        ans = {}
        for i in words:
            val = returnSorted(i)
            if val in ans:
                ans[val].append(i)
            else:
                ans[val] = [i]
        return list(ans.values())