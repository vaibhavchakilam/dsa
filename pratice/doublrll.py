class Node:
    def __init__(self,Data):
        self.Data = Data
        self.Next = None
        self.prev = None
        
def traves(head):
         currentNode = head
         while currentNode is not None:
             print(currentNode.Data,end=" ->")
             currentNode = currentNode.Next
         print("NULL")   
           
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.Next = n2
n2.prev = n1
n2.Next = n3
n3.prev = n2
n3.Next = n4

traves(n1)