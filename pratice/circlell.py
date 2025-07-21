class Node:
  def __init__(self,Data):
    self.Data = Data
    self.Next = None
    
def circle(head):
    currentNode =head
    startNode = head
    while  currentNode!= startNode:
        print(currentNode.Data,end="->")
        
        
    print(".........")
n1 =Node(1)    
n2 =Node(2)    
n3 =Node(3)    
n4 =Node(4)    
n5 =Node(5)

n1.Next =n2
n2.Next =n3
n3.Next =n4
n4.Next =n5
n5.Next =n1

circle(n1)
    
    
    
    