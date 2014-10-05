import unittest
""" Binary tree """

class BinaryNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    
    def add(self, value):
        if value < self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryNode(value)
        if value > self.value:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryNode(value)
    
    def get_max_left(self):
        node = self.left
        child = node.right
        if child:
            while child.right:
                node = child
                child = child.right
            return child, node
        else:
            return None, node
    
    def delete(self):
        if self.right == None and self.left == None:
            self.value = None
            return None
        elif self.right == None:
            return self.left
        else:
            self.left == None
            return self.right
        
        max_grandchild, max_child = self.get_max_left()
        if max_grandchild:
            self.value = max_grandchild.value
            max_child.right = max_grandchild.left
        else:
            self.left = max_child.left
            self.value = max_child.value
        return self

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
    
    def contains(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right  
            
        return False
    
    
    def delete (self, value):
        if self.root and self.contains(value):
            self.root = self.delete_node(self.root, value)
            return True
        return None
        
    def delete_node(self, parent, value):
        if parent == None:
            return None    
        if value == parent.value:
            return parent.delete()
        elif value < parent.value:
            parent.left = self.delete_node(parent.left, value)
        else:
            parent.right = self.delete_node(parent.right, value)
        return parent
        
            
                
class TestBinaryTree(unittest.TestCase):
    """ This class is for checking if is_palin fuction works well for one palin and
        one not palindrome  """

    def setUp(self):
        self.values=[3, 1, 2, 6, 4, 3, 7, 19, 21]
        self.BST = BinaryTree()
        for i in self.values:
            self.BST.add(i)
        
    def tearDown(self):
        self.values = None
        self.BST = None
        
    def test_add_contains(self):
        for i in self.values:
            self.assertEqual(self.BST.contains(i), True)
        self.assertEqual(self.BST.contains(18), False)
    
    def test_delete_leaves(self):
        self.assertEqual(self.BST.delete(6), True)
        self.assertEqual(self.BST.delete(18), None)
        

""" TEST SUITE DEF """
def suite():
    tests = ['test_add_contains', 'test_delete_leaves']

    return unittest.TestSuite(map(TestBinaryTree, tests))

""" RUNNING TESTS """
test_suite = suite()
unittest.TextTestRunner(verbosity=2).run(test_suite)
