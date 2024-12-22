import random
import time
from AVL import AVLTree
from redblack import RedBlackTree
from binary import BinarySearchTree

def compare_tree_heights(num_elements):

    data = random.sample(range(1, num_elements + 1), num_elements)

    avl_tree = AVLTree()
    avl_tree.root = None
    rb_tree = RedBlackTree()
    binary_tree = BinarySearchTree()



    for value in data:
        avl_tree.root = avl_tree.insert(avl_tree.root, value)
        rb_tree.insert(value)
        binary_tree.insert(value)

    avl_height = avl_tree.get_height(avl_tree.root)
    rb_height = rb_tree.height(rb_tree.root)
    binary_height = binary_tree.height(binary_tree.root)

    return avl_height, rb_height, binary_height

if __name__ == "__main__":
    num_elements = 1000  
    avl_height, rb_height, binary_height = compare_tree_heights(num_elements)

    print(f"Height of AVL Tree: {avl_height}")
    print(f"Height of Red-Black Tree: {rb_height}")
    print(f"Height of Binary Tree: {binary_height}")

    rb_tree1 = RedBlackTree()

    fixed_data = [i for i in range(1, 10001)] 

    for val in fixed_data:
        rb_tree1.insert(val)

    fixed_inserts = [10001 + i for i in range(1, 2001)]  
    fixed_deletes = [5000 + i for i in range(1, 2001)]

    total_insertion_time_rb = 0
    for val in fixed_inserts:
        total_insertion_time_rb += rb_tree1.insert(val)

    total_deletion_time_rb = 0  
    for key in fixed_deletes:
        total_deletion_time_rb += rb_tree1.delete(key)

    print(f"Total insertion time rb: {total_insertion_time_rb:.5f} seconds")
    print(f"Total deletion time rb: {total_deletion_time_rb:.5f} seconds")

    avl_tree = AVLTree()
    avl_tree.root = None

    fixed_data = [i for i in range(1, 10001)]  

    for val in fixed_data:
        avl_tree.root = avl_tree.insert(avl_tree.root, val)

    total_insertion_time_avl = 0
    start_time = time.time()
    for _ in range(10):
        for val in fixed_inserts:
            avl_tree.root = avl_tree.insert(avl_tree.root, val)
    end_time = time.time()
    total_insertion_time_avl += (end_time - start_time)
    total_insertion_time_avl = total_insertion_time_avl / 10

    total_deletion_time_avl = 0
    start_time = time.time()
    for _ in range(10):
        for key in fixed_deletes:
             avl_tree.root = avl_tree.delete(avl_tree.root, key)
    end_time = time.time()
    total_deletion_time_avl += (end_time - start_time)
    total_deletion_time_avl = total_deletion_time_avl / 10

    print(f"Total insertion time avl: {total_insertion_time_avl:.5f} seconds")
    print(f"Total deletion time avl: {total_deletion_time_avl:.5f} seconds")

