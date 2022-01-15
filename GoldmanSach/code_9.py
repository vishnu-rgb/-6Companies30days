#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        st = ""
        i = 0
        num = 1
        if S[0] == "I":
            st += str(num)
            num += 1
        while i < len(S):
            if S[i] == "I":
                j = i
                count = 0
                while j < len(S):
                    if S[j] == "I":
                        j += 1
                        count += 1
                    else:
                        break
                for p in range(count-1):
                    st += str(num)
                    num += 1
                i = j
            elif S[i] == "D":
                j = i
                count = 0
                while j < len(S):
                    if S[j] == "D":
                        j += 1
                        count += 1
                    else:
                        break
                before = num
                num = num + count
                after = num
                while num >= before:
                    st += str(num)
                    num -= 1
                num = after+1
            i = j
        if S[-1] == "I":
            st += str(num)
        return st