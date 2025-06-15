class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if n <= 0:
            raise IndexError("Index should be 1 or greater.")

        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range.")

        print(f"Deleting node at position {n} with value {current.data}")
        prev.next = current.next



if __name__ == "__main__":
    ll = LinkedList()

    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Initial list:")
    ll.print_list()

    Delete 2nd node
    ll.delete_nth_node(2)

    print("\nAfter deleting 2nd node:")
    ll.print_list()
