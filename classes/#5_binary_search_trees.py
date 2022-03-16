TODO
'''
A Tree consists of a root, which is of type Node, 
and possibly a left subtree of type Tree and possibly a right subtree of type Tree. 

If the left subtree is present, then all its nodes are less than the parent tree's root 
and if the right tree is present, then all its nodes are greater than the parent tree's root. 

In this kata, classes Tree and Node have been provided. 
However, the methods __eq__, __ne__, and __str__ are missing from the Tree class. 
Your job is to provide the implementation of these methods. 

The example test cases should provide enough information to implement these methods correctly.
'''

class Tree(object):
    
    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left: assert type(left) == Tree and left.root < root
        if right: assert type(right) == Tree and root < right.root

        self.left = left
        self.root = root
        self.right = right
        
    def is_leaf(self):
        return not(self.left or self.right)
        
    
    def __str__(self):
        # return string output 
        # return '[_ B [C]]'
        return str(self.root)
    
    def __eq__(self, other):
        # return when trees are equal
        pass
    
    def __ne__(self, other):
        # return when not equal
        pass

class Node(object):
    
    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight
    
    def __str__(self):
        return str(self.value)   
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __eq__(self, other):
        return self.value == other.value 

    def __ne__(self, other):
        return self.value != other.value 

print(Node('A'))
tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
tree2 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
print(tree1)
print(Tree(Node('B'), None, Tree(Node('C'))))

'''
Tree(Node('B'), None, Tree(Node('C'))))
'[_ B [C]]'
when one subtree, but not both, is missing, an underscore is in its place, 
a single space separates the root node from the subtrees, and
'''
