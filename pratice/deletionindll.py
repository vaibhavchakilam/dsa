class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None
        self.prev = None

def traves(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.Data, end=" -> ")
        currentNode = currentNode.Next
    print("NULL")

def delete_at_end(head):
    if head is None:
        print("List is empty")
        return None

    if head.Next is None:
        return None

    currentNode = head
    while currentNode.Next is not None:
        currentNode = currentNode.Next

    currentNode.prev.Next = None

    return head

# create: 1 <-> 2 <-> 3 <-> 4
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.Next = n2
n2.prev = n1
n2.Next = n3
n3.prev = n2
n3.Next = n4
n4.prev = n3

traves(n1)
n1 = delete_at_end(n1)  # delete last node
traves(n1)
