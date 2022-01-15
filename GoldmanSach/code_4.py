# Run length Encode https://practice.geeksforgeeks.org/problems/run-length-encoding/1/#
def encode(arr):
    i = 0
    ans = ""
   
    while i < len(arr):
       temp = arr[i]
       cnt = 1
       while i + 1 < len(arr) and temp == arr[i + 1]:
           i += 1
           cnt += 1
       ans += temp + str(cnt)
       i += 1
    return ans
                
            