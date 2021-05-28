class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, \
                          self.left, \
                          self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0], None, None)
        for elem in tree_data[1:]:
            self.insert(self.root, elem)
 
    def data(self):
        return self.root

    def sorted_data(self):
        def sorted(node):
            if node is None:
                return []
            else:
                return sorted(node.left) + \
                             [node.data] + \
                             sorted(node.right)
        return sorted(self.root)

    def insert(self, node, elem):
        def insertRight(node, elem):
            if node.right is None:
                node.right = TreeNode(elem, None, None)
            else:
                self.insert(node.right, elem)
        def insertLeft(node, elem):
            if node.left is None:
                node.left = TreeNode(elem, None, None)
            else:
                self.insert(node.left, elem)
        if (elem <= node.data):
            insertLeft(node, elem)
        else:
            insertRight(node, elem)
