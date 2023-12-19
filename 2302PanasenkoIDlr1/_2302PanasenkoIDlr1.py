class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_to_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def add_to_start(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def delete_last(self):
        if self.head is None:
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        self.size -= 1

    def delete_first(self):
        if self.head is None:
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        self.size -= 1

    def insert_at_index(self, data, index):
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.add_to_start(data)
        elif index == self.size:
            self.add_to_end(data)
        else:
            new_node = Node(data)
            current = self.head
            for i in range(index):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1

    def get_at_index(self, index):
        if index < 0 or index >= self.size:
            return None
        
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.delete_first()
        elif index == self.size - 1:
            self.delete_last()
        else:
            current = self.head
            for i in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1

    def get_size(self):
        return self.size

    def delete_all(self):
        self.head = None
        self.tail = None
        self.size = 0

    def replace_at_index(self, data, index):
        if index < 0 or index >= self.size:
            return
        
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data

    def is_empty(self):
        return self.size == 0

    def reverse(self):
        if self.head is None or self.head == self.tail:
            return
        
        current = self.head
        while current is not None:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            
            current = temp
        
        self.head, self.tail = self.tail, self.head

    def insert_list_at_index(self, linked_list, index):
        if index < 0 or index > self.size:
            return
        
        if linked_list is None or linked_list.is_empty():
            return
        
        if index == 0:
            linked_list.tail.next = self.head
            self.head.prev = linked_list.tail
            self.head = linked_list.head
        elif index == self.size:
            self.tail.next = linked_list.head
            linked_list.head.prev = self.tail
            self.tail = linked_list.tail
        else:
            current = self.head
            for i in range(index):
                current = current.next
            linked_list.head.prev = current.prev
            linked_list.tail.next = current
            current.prev.next = linked_list.head
            current.prev = linked_list.tail
        self.size += linked_list.size

    def insert_list_at_end(self, linked_list):
        self.insert_list_at_index(linked_list, self.size)

    def insert_list_at_start(self, linked_list):
        self.insert_list_at_index(linked_list, 0)

    def contains_list(self, linked_list):
        if linked_list is None or linked_list.is_empty():
            return False
        
        current = self.head
        while current is not None:
            if current.data == linked_list.head.data:
                temp_current = current
                temp_linked_list = linked_list.head
                while temp_current is not None and temp_linked_list is not None:
                    if temp_current.data != temp_linked_list.data:
                        break
                    temp_current = temp_current.next
                    temp_linked_list = temp_linked_list.next
                if temp_linked_list is None:
                    return True
            current = current.next
        return False

    def find_first_index_of_list(self, linked_list):
        if linked_list is None or linked_list.is_empty():
            return -1
        
        current = self.head
        index = 0
        while current is not None:
            if current.data == linked_list.head.data:
                temp_current = current
                temp_linked_list = linked_list.head
                while temp_current is not None and temp_linked_list is not None:
                    if temp_current.data != temp_linked_list.data:
                        break
                    temp_current = temp_current.next
                    temp_linked_list = temp_linked_list.next
                if temp_linked_list is None:
                    return index
            current = current.next
            index += 1
        return -1

    def find_last_index_of_list(self, linked_list):
        if linked_list is None or linked_list.is_empty():
            return -1
        
        current = self.tail
        index = self.size - 1
        while current is not None:
            if current.data == linked_list.tail.data:
                temp_current = current
                temp_linked_list = linked_list.tail
                while temp_current is not None and temp_linked_list is not None:
                    if temp_current.data != temp_linked_list.data:
                        break
                    temp_current = temp_current.prev
                    temp_linked_list = temp_linked_list.prev
                if temp_linked_list is None:
                    return index - linked_list.size + 1
            current = current.prev
            index -= 1
        return -1

    def swap_elements_at_index(self, index1, index2):
        if index1 < 0 or index1 >= self.size or index2 < 0 or index2 >= self.size:
            return
        
        if index1 == index2:
            return
        
        if index1 > index2:
            index1, index2 = index2, index1
        
        current1 = self.head
        for i in range(index1):
            current1 = current1.next
        
        current2 = self.head
        for i in range(index2):
            current2 = current2.next
        
        current1.data, current2.data = current2.data, current1.data
        
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()
