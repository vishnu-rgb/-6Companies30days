def maxDepth(self, node):
        if node is None:
            return 0
        return 1 + max((self.maxDepth(node.left), self.maxDepth(node.right)))
    
    def dfs(self, node, target):
        if node is None:
            return (0,0)
        if node.data == target:
            ans = self.maxDepth(node.right)
            ans = max(ans, self.maxDepth(node.left))
            return (ans,1)
        ans, dist = self.dfs(node.left, target)
        if dist:
            ans = max( ans, dist+self.maxDepth(node.right) )
            return (ans,dist+1)
        
        ans, dist = self.dfs(node.right, target)
        if dist:
            ans = max( ans, dist+self.maxDepth(node.left) )
            return (ans,dist+1)
        return (0,0)
    
    def minTime(self, root, target):
        # code here
        return (self.dfs(root,target))[0]