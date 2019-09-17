class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.helper_insert(self.root, new_val)

    def search(self, find_val):
        return self.helper_search(self.root, find_val)
        
    def print_BST(self):
        print(" - ".join(map(str, self.helper_print_BST(self.root, []))))
        
    def helper_insert(self, start, new_val):
        if new_val < start.value:
            if start.left:
                self.helper_insert(start.left, new_val)
            else:
                start.left = Node(new_val)
        else:
            if start.right:
                self.helper_insert(start.right, new_val)
            else:
                start.right = Node(new_val)
    
    def helper_search(self, start, find_val):
        # print(start.value, find_val)
        if start.value == find_val:
            return True
        elif find_val < start.value and start.left and self.helper_search(start.left, find_val):
            return True
        elif find_val > start.value and start.right and self.helper_search(start.right, find_val):
            return True
        else:
            return False
            
                
    def helper_print_BST(self, start, traversal):
        traversal.append(start.value)
        if start.left:
            self.helper_print_BST(start.left, traversal)
        if start.right:
            self.helper_print_BST(start.right, traversal)
        return traversal
        
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
# tree.print_BST()

# Check search
# Should be True
print tree.search(3)
# Should be False
print tree.search(6)
