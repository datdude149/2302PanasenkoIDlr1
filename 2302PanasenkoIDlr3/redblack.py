import time

class Node:
    def __init__(self, key):
        self.data = key
        self.color = 'red'  
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(0) 
        self.NIL_LEAF.color = 'black'
        self.root = self.NIL_LEAF
    
    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF

        parent = None
        current = self.root

        while current != self.NIL_LEAF:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        
        if parent is None:  
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red' 

        start_time = time.time()
        self.insert_fixup(new_node)
        end_time = time.time()
        
        return end_time - start_time  

    def insert_fixup(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:  
                uncle = node.parent.parent.right
                if uncle.color == 'red':  
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:  
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'  
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:  
                uncle = node.parent.parent.left
                if uncle.color == 'red': 
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left: 
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'  
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL_LEAF:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def delete(self, key):
        node_to_delete = self.search(self.root, key)
        if node_to_delete == self.NIL_LEAF:
            return

        y = node_to_delete
        original_color = y.color
        if node_to_delete.left == self.NIL_LEAF:
            x = node_to_delete.right
            self.transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL_LEAF:
            x = node_to_delete.left
            self.transplant(node_to_delete, node_to_delete.left)
        else:
            y = self.minimum(node_to_delete.right)
            original_color = y.color
            x = y.right
            if y.parent == node_to_delete:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y
            self.transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.color = node_to_delete.color

        start_time = time.time()
        if original_color == 'black':
            self.delete_fixup(x)
        end_time = time.time()
        
        return end_time - start_time 

    def delete_fixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL_LEAF:
            node = node.left
        return node

    def search(self, node, key):
        if node == self.NIL_LEAF or key == node.data:
            return node
        elif key < node.data:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def height(self, node):
        if node == self.NIL_LEAF:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def inorder(self, node):
        return self.inorder(node.left) + [node.data] + self.inorder(node.right) if node != self.NIL_LEAF else []

    def preorder(self, node):
        return [node.data] + self.preorder(node.left) + self.preorder(node.right) if node != self.NIL_LEAF else []

    def postorder(self, node):
        return self.postorder(node.left) + self.postorder(node.right) + [node.data] if node != self.NIL_LEAF else []

    def level_order(self):
        if not self.root or self.root == self.NIL_LEAF:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left != self.NIL_LEAF:
                queue.append(node.left)
            if node.right != self.NIL_LEAF:
                queue.append(node.right)
        return result

    def print_tree(self, node, level=0, label="Root"):
        if node != self.NIL_LEAF:
            print(" " * (level * 4) + f"{label}: {node.data} ({node.color})")
            self.print_tree(node.left, level + 1, "L")
            self.print_tree(node.right, level + 1, "R")


def main():
    rb_tree = RedBlackTree()

    fixed_data = [i for i in range(1, 6)] 

    for val in fixed_data:
        rb_tree.insert(val)

    print("\nДерево:")
    rb_tree.print_tree(rb_tree.root)

    print(f"\nВысота дерева: {rb_tree.height(rb_tree.root)}")

    print(f"Обход в глубину (inorder): {rb_tree.inorder(rb_tree.root)}")
    print(f"Обход в глубину (preorder): {rb_tree.preorder(rb_tree.root)}")
    print(f"Обход в глубину (postorder): {rb_tree.postorder(rb_tree.root)}")
    print(f"Обход в ширину (level order): {rb_tree.level_order()}")

    print(f"\nВысота дерева: {rb_tree.height(rb_tree.root)}")

if __name__ == "__main__":
    main()
