# Node class represents each element in the doubly linked list
class Node:
    def __init__(self, data):
        self.prev = None  # Reference to previous node
        self.data = data  # Data stored in the node
        self.next = None  # Reference to next node

# DLinkList class implements the doubly linked list functionality
class DLinkList:
    def __init__(self):
        self.head = None  # Points to the first node in the list
        self.tail = None  # Points to the last node in the list
        self.size = 0     # Keeps track of the number of nodes

    def add_at_tail(self, data):
        """Add a new node at the end of the list"""
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            self.tail = new_node
        else:  # If list has at least one node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def add_at_head(self, data):
        """Add a new node at the beginning of the list"""
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            self.tail = new_node
        else:  # If list has at least one node
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def add_at_middle(self, data, position):
        """Add a new node at a specified position in the list"""
        # Check if position is valid
        if position < 0 or position > self.size:
            raise ValueError("Invalid position")
        
        # Handle special cases
        if position == 0:
            self.add_at_head(data)
            return
        if position == self.size:
            self.add_at_tail(data)
            return

        # Insert at specified position
        new_node = Node(data)
        current = self.head
        # Traverse to the position
        for _ in range(position - 1):
            current = current.next
        
        # Update links to insert new node
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        self.size += 1

    def search(self, data):
        """Search for a node with given data and return its position"""
        current = self.head
        position = 0
        # Traverse the list
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1  # Return -1 if data not found

    def print(self):
        """Print all nodes in the list"""
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Test cases
if __name__ == "__main__":
    my_linked_list = DLinkList()
    
    # Testing add_at_tail
    my_linked_list.add_at_tail("Node one")
    my_linked_list.add_at_tail("Node two")
    my_linked_list.add_at_tail("Node three")
    
    # Testing add_at_head
    my_linked_list.add_at_head("New Head")
    
    # Testing add_at_middle
    my_linked_list.add_at_middle("Middle Node", 2)
    
    # Testing search
    print(f"Position of 'Node two': {my_linked_list.search('Node two')}")
    
    print("\nPrinting all nodes:")
    my_linked_list.print()