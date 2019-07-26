# Consideration: Do both lists use capitalization equally? Yes. But in unknown data sets, should convert to all caps to avoid missed duplicates from casing differences. Can use upper() when creating tree, and .title() before printing duplicate list
# Edge Case: One or both lists are empty? Still prints nothing.
# Edge Case: No duplicates found. Print nothing or error message?
# Consideration: This BST does not allow for duplicates in the tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        print(f"Value: {self.value}")

class Balanced_BST:
    def __init__(self):
        # Sets a root node
        self.root = None
        # Sets the height at -1, so when we add a node, the height is 0
        self.height = -1
        # Tracks the balance to know when the tree needs re-balancing
        self.balance = 0
    
    def insert(self, value):
        # Create a new node
        node = Node(value)

        # If tree has no nodes
        if not self.root:
            self.root = node
            # Create sub-trees on each side of the root
            self.root.left = Balanced_BST()
            self.root.right = Balanced_BST()
        # if passed value is < current root, insert to the left 
        elif value < self.root.value:
            self.root.left.insert(value)
        # if passed value is > current root, insert to the right
        elif value > self.root.value:
            self.root.right.insert(value)
        # Else value is already in the tree and no duplicates

        # Check if the tree needs to be rebalanced
        self.rebalance()

    def rebalance(self):
        pass
    
    def rotate_right(self):
        pass
    
    def rotate_left(self):
        pass
    