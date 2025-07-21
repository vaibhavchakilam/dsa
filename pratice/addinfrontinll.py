class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

def traverse(head):
    currentnode = head  
    while currentnode is not None:
        print(currentnode.Data, end="->")  
        currentnode = currentnode.Next
    print("NULL")

def insert_at_front(head, data):
    new_node = Node(data)
    new_node.Next = head
    return new_node   # new head of the list



# Create initial list
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

Node1.Next = Node2
Node2.Next = Node3
Node3.Next = Node4
Node4.Next = Node5

print("Original list:")
traverse(Node1)

# Insert 0 at front
Node1 = insert_at_front(Node1, 0)

print("\nAfter inserting 0 at front:")
traverse(Node1)

# Insert 50 at end


print("\nAfter inserting 50 at end:")
traverse(Node1)
