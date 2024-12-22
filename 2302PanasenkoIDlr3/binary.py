class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def height(self, node):
        if node is None:
            return -1  
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1

    def inorder(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []

    def preorder(self, node):
        return [node.val] + self.preorder(node.left) + self.preorder(node.right) if node else []

    def postorder(self, node):
        return self.postorder(node.left) + self.postorder(node.right) + [node.val] if node else []

    def level_order(self):
        if not self.root:
            return []
        result, queue = [], [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
    
    def print_tree(self, node, level=0, label="Root"):
            if node is not None:
                print(" " * (level * 4) + f"{label}: {node.val}")
                self.print_tree(node.left, level + 1, "L")
                self.print_tree(node.right, level + 1, "R")

def main():
    bst = BinarySearchTree()
    nodes = [15, 10, 20, 8, 12, 17, 25]
    for node in nodes:
        bst.insert(node)

    print("Высота дерева:", bst.height(bst.root))
    print("Обход в глубину (inorder):", bst.inorder(bst.root))
    print("Обход в глубину (preorder):", bst.preorder(bst.root))
    print("Обход в глубину (postorder):", bst.postorder(bst.root))
    print("Обход в ширину (level order):", bst.level_order())
    print("\nВывод дерева:", bst.print_tree(bst.root))

if __name__ == "__main__":
    main()
