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
 
def deleteinend(head):
    currentnode = head  
    while currentnode.Next.Next is not None:
     currentnode = currentnode.Next 
    currentnode.Next = None  
    return head

    
          
    


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


deleteinend(Node1)
traverse(Node1)





