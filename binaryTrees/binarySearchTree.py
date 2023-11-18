#import pdb

class Node:
    def __init__(self, value):
        # Node class to represent each node in the Binary Search Tree
        self.value = value  # Initialize node with a value
        self.left = None    # Initialize left child as None
        self.right = None   # Initialize right child as None



class BinarySearchTree:
    def __init__(self):
        # BinarySearchTree class to manage the tree
        self.root = None  # Initialize the root of the tree as None (empty tree)

    def insert(self, value):
        # Method to insert a new value into the BST
        if self.root is None:  # If the tree is empty
            self.root = Node(value)  # Set the new value as the root
        else:
            self._insert_recursive(value, self.root)  # Call the recursive helper function

    def _insert_recursive(self, value, current_node):
        # Recursive helper function to insert a value into the BST
        if value < current_node.value:  # If the value is less than the current node's value
            if current_node.left is None:  # If left child is None
                current_node.left = Node(value)  # Insert the new value as the left child
            else:
                # Recursively call _insert_recursive for the left subtree
                self._insert_recursive(value, current_node.left)
        elif value > current_node.value:  # If the value is greater than the current node's value
            if current_node.right is None:  # If right child is None
                current_node.right = Node(value)  # Insert the new value as the right child
            else:
                # Recursively call _insert_recursive for the right subtree
                self._insert_recursive(value, current_node.right)
        else:
            # The value already exists in the tree, handle it as needed
            pass

    def search(self, value):
        # Method to search for a value in the BST
        #pdb.set_trace()
        return self._search_recursive(value, self.root) if self.root else None

    def _search_recursive(self, value, current_node):
        # Recursive helper function to search for a value in the BST
        if current_node is None or value == current_node.value:  # If current node is None or found
            return current_node  # Return the node
        elif value < current_node.value:  # If the value is less than the current node's value
            return self._search_recursive(value, current_node.left)  # Search left subtree
        else:
            return self._search_recursive(value, current_node.right)  # Search right subtree

# Example of usage:
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)

found_node = bst.search(9)
print("Node found:", found_node.value if found_node else "Not found")



