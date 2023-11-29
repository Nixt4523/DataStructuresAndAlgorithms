# Binary Trees
"""
Binary Tree is a Non-Linear Dat Structure
It consists or Root node, Parent nodes, Child nodes, Leaf nodes and Sibling nodes
In Binary Tree each Node can only have 0, 1 or 2 Nodes and each child can only have 1 Parent node
Most common Tree is a Binary Search Tree, Binary Search Tree is a Subset of Binary Tree
All child nodes in the BST to the right of the Root node must be Greater than current node
A node in a BST can only have up to 2 Child nodes
"""

'''
Time complexities of BST Functions in a Balanced Tree
Lookup Function : O(log n)
Insertion Function : O(log n)
Deletion Function : O(log n)

Time complexities of BST Functions in a Unbalanced Tree
Lookup Function : O(n)
Insertion Function : O(n)
Deletion Function : O(n)
'''

'''
Advantages of BST
Operations with better time complexities than O(n)
Ordered and Structured
Flexible size
'''

'''
Disadvantages of BST
No O(1) Operations
'''


# Implementing BST in Python
# First we need to create Node class to store Data and the left and the right Child nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None


# After creating Node class we need to create BST class
class BST:

    # Initializing Root node of the BST
    def __init__(self):
        self.root_node = None

    # Function to insert node in the BST
    def insert_node(self, data):
        new_node = Node(data)

        if self.root_node is None:
            self.root_node = new_node
        else:
            curr_node = self.root_node
            not_inserted = True
            while not_inserted:
                if data < curr_node.data:
                    if not curr_node.left_node:
                        curr_node.left_node = new_node
                        not_inserted = False
                    curr_node = curr_node.left_node
                else:
                    if not curr_node.right_node:
                        curr_node.right_node = new_node
                        not_inserted = False
                    curr_node = curr_node.right_node

    # Function to find a node in the BST
    def lookup_node(self, data):

        if not self.root_node:
            print('Tree is Empty!')

        curr_node = self.root_node

        while curr_node:
            if data < curr_node.data:
                curr_node = curr_node.left_node
            elif data > curr_node.data:
                curr_node = curr_node.right_node
            elif curr_node.data == data:
                print(f'Found : {data}')
                return curr_node
        print(f'Not Found : {data}')
        return None

    # Function to remove node from BST
    def remove_node(self, root, data):

        if not root:
            root = self.root_node

        root_node = root

        if not root_node:
            return None

        if root_node.data == data:
            if not root_node.left_node and not root_node.right_node:
                return None
            if not root_node.left_node and root_node.right_node:
                return root_node.right_node
            if not root_node.right_node and root_node.left_node:
                return root_node.left_node

            ref_node = root_node.right_node

            while ref_node.left_node:
                ref_node = ref_node.left_node

            root_node.data = ref_node.data
            root_node.right_node = self.remove_node(root_node.right_node, root_node.data)

        elif root_node.data > data:
            root_node.left_node = self.remove_node(root_node.left_node, data)
        else:
            root_node.right_node = self.remove_node(root_node.right_node, data)

    # Function to print the BST
    def print_tree(self, node):

        tree = {"data": node.data, "right_node": None, "left_node": None}

        if node.left_node is None:
            tree['left_node'] = None
        else:
            tree['left_node'] = self.print_tree(node.left_node)

        if node.right_node is None:
            tree['right_node'] = None
        else:
            tree['right_node'] = self.print_tree(node.right_node)

        print(tree)
        return tree


'''
We can initialize the Binary Search Tree i.e BST()
We can use BST methods in Binary Search Tree class to manipulate the Tree
'''

# Binary Search Tree Questions

# Question 1
'''
You have given a root node reference of the Binary Search Tree and a key i.e data
Delete the given key from the given Binary Search Tree
Return the root node reference of the Binary Search Tree
Input : root = [5, 3, 6, 2, 4, null, 7], key = 3
Output : [5, 4, 6, 2, null, null, 7]
Link : https://leetcode.com/problems/delete-node-in-a-bst/
'''


class Solution:
    def delete_node(self, root, key):

        root_node = root

        # Checking if root node exist
        if not root_node:
            return None

        # Condition 1 if root node's value is equal to key
        if root_node.val == key:

            # Condition 1 if root node does not have any Child nodes
            if not root_node.left and not root_node.right:
                return None

            # Condition 2 if root node have right child but not left child
            if not root_node.left and root_node.right:
                return root_node.right

            # Condition 3 if root node have left child but not right child
            if not root_node.right and root_node.left:
                return root_node.left

            ref_node = root_node.right

            # Traversing to the tree to get the largest value
            while ref_node.left:
                ref_node = ref_node.left

            root_node.val = ref_node.val

            root_node.right = self.delete_node(root_node.right, root_node.val)

        # Condition 2 if root node's value is greater than key
        elif root_node.val > key:
            root_node.left = self.delete_node(root_node.left, key)

        # Condition 3 if root node's value is greater than key
        else:
            root_node.right = self.delete_node(root_node.right, key)

        return root_node