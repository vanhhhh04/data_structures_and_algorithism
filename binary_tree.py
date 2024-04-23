class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
         else:
            self.data = data
# Print the Tree

# Left -> Root -> Right
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data)
      if self.right:
         self.right.PrintTree()
# Preorder traversal
# Root -> Left ->Right
   def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res
# Left ->Right -> Root
   def PostorderTraversal(self, root):
    res = []
    if root:
        res = self.PostorderTraversal(root.left)
        res = res + self.PostorderTraversal(root.right)
        res.append(root.data)
    return res

   def findval(self, val):
      if val < self.data :
         if self.left is None :
            return str(val) + "is not found"
         else :
            return self.left.findval(val)
      elif val > self.data :
            if self.right is None :
               return str(val) +"is not found"
            else :
               return self.right.findval(val)
      else :
         print(str(self.data) + ' is found')


   def find_min(self):
      if self.left is None :
         print(self.data)
      else :
         self.left.find_min()

   def find_max(self):
      if self.right is None :
         print(self.data)
      else :
         self.right.find_max()

   def calculate_sum(self):
      left_sum = self.left.calculate_sum() if self.left else 0
      right_sum = self.right.calculate_sum() if self.right else 0
      return self.data + left_sum + right_sum


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
# print(root.PrintTree())
# print(root.PreorderTraversal(root))
root.findval(14)
root.find_min()
root.find_max()
print(root.calculate_sum())
