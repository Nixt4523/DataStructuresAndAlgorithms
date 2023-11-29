class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

class BST:

    def __init__(self):
        self.root_node = None

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

    def breadth_first_search(self):

        curr_node = self.root_node
        array = []
        queue = []

        queue.append(curr_node)

        while len(queue) > 0:
            curr_node = queue.pop(0)
            array.append(curr_node.data)

            if curr_node.left_node:
                queue.append(curr_node.left_node)

            if curr_node.right_node:
                queue.append(curr_node.right_node)

        print(array)


tree = BST()
tree.insert_node(9)
tree.insert_node(4)
tree.insert_node(6)
tree.insert_node(20)
tree.insert_node(170)
tree.insert_node(15)
tree.insert_node(1)
tree.breadth_first_search()

