class Node:
    def __init__(self,Data):
        self.Data = Data
        self.Next = None
        
def addatsp(head,data,index):
            currentNode = head
            newnode = Node(data)
            count = 0
            while currentNode and count<index-2:
             currentNode =  currentNode.Next
             count+=1
            newnode.Next = currentNode.Next
            currentNode.Next = newnode
            return head
def traverse(head):
    currentnode = head  
    while currentnode is not None:
        print(currentnode.Data, end="->")  
        currentnode = currentnode.Next
    print("NULL")

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

Node1.Next = Node2
Node2.Next = Node3
Node3.Next = Node4
Node4.Next = Node5

addatsp(Node1,10,3)
traverse(Node1)
        