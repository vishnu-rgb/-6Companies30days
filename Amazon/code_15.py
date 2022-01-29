# Function shouldn't return anything

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def skipMdeleteN(self, head, M, N):
        curr = head
        while curr:
            for _ in range(1, M):
                if curr and curr.next:
                    curr = curr.next
            temp = curr.next
            for _ in range(1, N+1):
                if temp:
                    temp = temp.next
            curr.next = temp
            curr = temp
        # Code here