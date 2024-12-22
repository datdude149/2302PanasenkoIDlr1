import time

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.height = 1  

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.data:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.get_balance(node)

        # Левый левый случай
        if balance > 1 and key < node.left.data:
            return self.right_rotate(node)
        # Правый правый случай
        if balance < -1 and key > node.right.data:
            return self.left_rotate(node)
        # Левый правый случай
        if balance > 1 and key > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        # Правый левый случай
        if balance < -1 and key < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def delete(self, root, key):
        if not root:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            temp = self.get_min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def pre_order(self, node):
        if node:
            print(node.data, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data, end=' ')
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=' ')

    def level_order(self, root):
        if not root:
            return

        queue = [root] 
        while queue:
            node = queue.pop(0) 
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)  
            if node.right:
                queue.append(node.right) 

    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            if node.left is not None or node.right is not None:  
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


def main():
    avl_tree = AVLTree()
    avl_tree.root = None

    fixed_data = [i for i in range(1, 6)]  

    for val in fixed_data:
        avl_tree.root = avl_tree.insert(avl_tree.root, val)

    height_of_tree = avl_tree.get_height(avl_tree.root)
    print(f"Высота дерева: {height_of_tree}")

    print("\nОбход в глубину (inorder): ", end="")
    avl_tree.in_order(avl_tree.root)
    print("\nОбход в глубину (preorder): ", end="")
    avl_tree.pre_order(avl_tree.root)
    print("\nОбход в глубину (postorder): ", end="")
    avl_tree.post_order(avl_tree.root)
    print("\nОбход в ширину (level order): ", end="")
    avl_tree.level_order(avl_tree.root)
    print("\n\nВывод дерева::")
    avl_tree.print_tree(avl_tree.root)

if __name__ == "__main__":
    main()
