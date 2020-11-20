class Solution:
    
    def isMirror(self,root1,root2):
        
        if(root1 == None or root2 == None):
            return root1 == root2
        
        if not (root1.val == root2.val):
            return False
        
        return (self.isMirror(root1.left,root2.right) and self.isMirror(root1.right,root2.left))
        
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if(root == None):
            return True
        return (self.isMirror(root.left,root.right))