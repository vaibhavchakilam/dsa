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

def insertNodeAtPosition(head, data, position):
    newnode = Node(data)
    if (position==1):
     newnode.prev = None
     newnode.Next = head
     head.prev = newnode
     return newnode

    currentNode = head
    count = 1
    while currentNode and count< position - 1:
        currentNode = currentNode.Next
        count = count + 1 
    
    temp = currentNode.Next
    currentNode.next = newnode
    newnode.prev = currentNode
    newnode.next = temp
    temp.prev = newnode
    
   # newnode.Next =currentNode.Next  
   # newnode.prev = currentNode  
   # currentNode.prev = newnode    
    return head
        
          
        
    
    



# Create initial list
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

print("Original list:")
traves(n1)


insertNodeAtPosition(n1, 25,3)

print("After insertion at beginning:")
traves(n1)
