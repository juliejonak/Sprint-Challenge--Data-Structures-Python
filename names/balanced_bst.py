# Consideration: Do both lists use capitalization equally? Yes. But in unknown data sets, should convert to all caps to avoid missed duplicates from casing differences. Can use upper() when creating tree, and .title() before printing duplicate list
# Edge Case: One or both lists are empty? Still prints nothing.
# Edge Case: No duplicates found. Print nothing or error message?
# Consideration: This BST does not allow for duplicates in the tree.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
    
    def __repr__(self):
        print(f"Value: {self.value}")


class Balanced_BST(object):
    
    def insert(self, root, value):
        # If tree has no nodes
        if not root:
            root = Node(value)
        # if passed value is < current root, insert to the left 
        elif value < root.value:
            root.left = self.insert(root.left, value)
        # if passed value is > current root, insert to the right
        elif value > root.value:
            root.right = self.insert(root.right, value)
        # Else value is already in the tree and no duplicates

        # Sets height to longest side +1
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Get the balance value of the root
        balance = self.getBalance(root)

        # if the balance leans left-left
        if balance > 1 and value < root.left.value:
            return self.rotate_right(root)
        # if the balance leans right-right
        if balance < -1 and value > root.right.value:
            return self.rotate_left(root)

        # if the balance leans left-right
        if balance > 1 and value > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # if the balance leans right-left
        if balance < -1 and value < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root


    def rotate_left(self, root):
        new_root = root.right
        T2 = new_root.left

        new_root.left = root
        root.right = T2

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        new_root.height = 1 + max(self.getHeight(new_root.left), self.getHeight(new_root.right))

        return new_root

    def rotate_right(self):
        new_root = root.left
        T2 = new_root.right

        new_root.right = root
        root.left = T2

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        new_root.height = 1 + max(self.getHeight(new_root.left), self.getHeight(new_root.right))

        return new_root

    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def contains(self, root, target):
        if root.value == target:
            return True
        
        if target < root.value:
            if not root.left:
                return False
            else:
                return self.contains(root.left, target)
        
        else:
            if not root.right:
                return False
            else:
                return self.contains(root.right, target)
    

tree = Balanced_BST()
root = None
test = [1,2,3,4,5,6,7]

print('inserting test data')
for key in test:
    root = tree.insert(root, key)
    print(f"Inserted {key}")
print(tree.contains(root, 6))