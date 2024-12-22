class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.tail:
            if self.tail == self.head:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1
            
    def shift(self):
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1

    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Индекс вне диапазона")
        if index == 0:
            self.prepend(value)
            return
        if index == self.size:
            self.append(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(index):
            current = current.next
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне диапазона")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне диапазона")
        if index == 0:
            self.shift()
            return
        if index == self.size - 1:
            self.pop()
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1

    def get_size(self):
        return self.size

    def clear(self):
        self.head = self.tail = None
        self.size = 0

    def set_at(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне диапазона")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def is_empty(self):
        return self.size == 0

    def reverse(self):
        current = self.head
        prev = None
        self.tail = current
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def insert_list_at(self, index, other_list):
        if not other_list or other_list.is_empty():
            return
        if index < 0 or index > self.size:
            raise IndexError("Индекс вне диапазона")
        current = other_list.head
        while current:
            self.insert_at(index, current.value)
            index += 1
            current = current.next

    def append_list(self, other_list):
        if other_list and not other_list.is_empty():
            for value in other_list:
                self.append(value)

    def prepend_list(self, other_list):
        if other_list and not other_list.is_empty():
            for value in reversed(other_list):
                self.prepend(value)

    def contains_list(self, other_list):
        if other_list.is_empty():
            return True
        current = self.head
        while current:
            match_found = True
            temp_current = current
            other_current = other_list.head
            while other_current:
                if not temp_current or temp_current.value != other_current.value:
                    match_found = False
                    break
                temp_current = temp_current.next
                other_current = other_current.next
            if match_found:
                return True
            current = current.next
        return False

    def index_of_list(self, other_list):
        if other_list.is_empty():
            return 0  
        current = self.head
        index = 0
        while current:
            match_found = True
            temp_current = current
            other_current = other_list.head
            while other_current:
                if not temp_current or temp_current.value != other_current.value:
                    match_found = False
                    break
                temp_current = temp_current.next
                other_current = other_current.next
            if match_found:
                return index
            current = current.next
            index += 1
        return -1  

    def last_index_of_list(self, other_list):
        if other_list.is_empty():
            return 0
        current = self.tail
        index = self.size - 1
        while current:
            match_found = True
            temp_current = current
            other_current = other_list.tail
            while other_current:
                if not temp_current or temp_current.value != other_current.value:
                    match_found = False
                    break
                temp_current = temp_current.prev
                other_current = other_current.prev
            if match_found:
                return index
            current = current.prev
            index -= 1
        return -1  

    def swap(self, index1, index2):
        if index1 < 0 or index1 >= self.size or index2 < 0 or index2 >= self.size:
            raise IndexError("Индекс вне диапазона")
        if index1 == index2:
            return  

        node1 = self.head
        for _ in range(index1):
            node1 = node1.next

        node2 = self.head
        for _ in range(index2):
            node2 = node2.next

        node1.value, node2.value = node2.value, node1.value

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

def print_list(dll):
    elements = [dll.get(i) for i in range(dll.get_size())]
    print("Текущий список:", elements)

def main():
    dll = DoublyLinkedList()

    dll.append(1)
    print("После добавления 1 в конец:")
    print_list(dll)

    dll.prepend(0)
    print("После добавления 0 в начало:")
    print_list(dll)

    dll.pop()
    print("После удаления последнего элемента:")
    print_list(dll)

    dll.shift()
    print("После удаления первого элемента:")
    print_list(dll)

    dll.append(2)
    dll.insert_at(1, 1.5)
    print("После вставки 1.5 по индексу 1:")
    print_list(dll)

    value = dll.get(1)
    print("Элемент по индексу 1:", value) 

    dll.remove_at(1)
    print("После удаления элемента по индексу 1:")
    print_list(dll)

    size = dll.get_size()
    print("Размер списка:", size) 

    dll.clear()
    print("После очистки списка:")
    print_list(dll)  

    print("Список пуст:", dll.is_empty()) 

    dll.append(1)
    dll.append(2)
    dll.append(3)
    print("После добавления 1, 2, 3:")
    print_list(dll)

    dll.reverse()
    print("После реверса списка:")
    print_list(dll)  

    other_list = DoublyLinkedList()
    other_list.append(4)
    other_list.append(5)
    dll.insert_list_at(1, other_list)
    print("После вставки другого списка (4, 5) по индексу 1:")
    print_list(dll)  

    contains = dll.contains_list(other_list)
    print("Содержит ли список другой список (4, 5):", contains) 

    index = dll.index_of_list(other_list)
    print("Индекс первого вхождения другого списка (4, 5):", index)  

    last_index = dll.last_index_of_list(other_list)
    print("Индекс последнего вхождения другого списка (4, 5):", last_index)  

    dll.swap(0, 2)
    print("После обмена элементов по индексам 0 и 2:")
    print_list(dll)   

if __name__ == "__main__":
    main()
