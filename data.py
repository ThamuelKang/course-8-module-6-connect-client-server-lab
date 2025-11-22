# Step 1: Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # points to the next node


# Step 2: LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Step 3: Append a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Step 4: Display the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Step 5: Recursive sum of all nodes
    def sum_nodes(self, node):
        if node is None:
            return 0
        return node.data + self.sum_nodes(node.next)

    # Step 6: Recursive search for a value
    def search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        return self.search(node.next, key)

    # Step 7: Recursive reverse
    def reverse(self, node):
        if node is None or node.next is None:
            return node
        new_head = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return new_head
