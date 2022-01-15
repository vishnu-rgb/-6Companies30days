# Greatest Common Divisor of string 
# link :https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        if not s: return t
        if not t: return s
        s, t = (s, t) if len(s) <= len(t) else (t, s)
        if t[:len(s)] == s:
            return self.gcdOfStrings(t[len(s):], s)
        return ''
        
            
            