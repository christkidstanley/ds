class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self, head_node):
        self.new_node = None
        self.head = head_node
        self.tail = self.head

    def insert(self, Node):
        self.head.next = Node
        self.head = Node

    def delete(self, value):
        previous_pointer = None
        if self.tail.data == value:
            self.tail = self.tail.next
        else:
            i_pointer = self.tail.next
            previous_pointer = self.tail
            while i_pointer is not None:
                if i_pointer.data == value:
                    previous_pointer.next = i_pointer.next
                    break
                previous_pointer = i_pointer
                i_pointer = i_pointer.next

    def print_ll(self):
        i_pointer = self.tail
        while i_pointer is not None:
            print(i_pointer.data)
            i_pointer = i_pointer.next

    def len_ll(self):
        n = 0
        i_pointer = self.tail
        while i_pointer is not None:
            n += 1
            i_pointer = i_pointer.next

        return n

    def swap(self, n1, n2):
        temp = n2.data
        n2.data = n1.data
        n1.data = temp

    def sort_ll(self):
        n = self.len_ll()
        i = 1
        key = self.tail.next
        while i < n:
            j = 0
            j_pointer = self.tail
            while j < i:
                if j_pointer.data > key.data:
                    self.swap(j_pointer, key)
                j_pointer = j_pointer.next
                j += 1
            key = key.next
            i += 1

    def create_cycle(self, n1):
        self.head.next = n1

    def find_cycle(self):
        rabbit_pointer = self.tail.next.next
        tortoise_pointer = self.tail
        while rabbit_pointer is not None and tortoise_pointer is not None:
            if rabbit_pointer == tortoise_pointer:
                print("True")
                break
            else:
                rabbit_pointer = rabbit_pointer.next.next
                tortoise_pointer = tortoise_pointer.next

    def rotate(self):
        i_pointer = self.tail
        while i_pointer is not None:
            if i_pointer.next == self.head:
                self.head.next = self.tail
                self.tail = self.head
                self.head = i_pointer
                i_pointer.next = None
            i_pointer = i_pointer.next

    def reverse(self):
        previous_pointer = None
        current_pointer = self.tail
        next_pointer = self.tail
        while current_pointer is not None:
            next_pointer = current_pointer.next
            current_pointer.next = previous_pointer
            previous_pointer = current_pointer
            current_pointer = next_pointer
        self.tail = previous_pointer


n1 = node(3)
l1 = linked_list(n1)
n2 = node(2)
l1.insert(n2)
n3 = node(0)
l1.insert(n3)
n4 = node(4)
l1.insert(n4)
l1.reverse()
l1.print_ll()