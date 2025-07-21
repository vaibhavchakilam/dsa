class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.reverse = None

def traverse(head):
    pointer = head
    while pointer:
        print(pointer.data,end="<-->")
        pointer = pointer.next
    print("Null")

def insertion(head,data,index):
    print("The Updated Double Linked List is: ")
    pointer = head
    count = 0
    node = Node(data)

    if (index == 0):
        pointer.reverse = node
        node.next = pointer
        head = node
        traverse(head)
        return

    while pointer and count < index-1:
        pointer = pointer.next
        count = count+1
    
    if (pointer.next == None):
        pointer.next = node
        node.reverse = pointer
        traverse(head)
        return

    node.next = pointer.next
    pointer.next = node
    node.reverse = pointer
    pointer = node.next
    pointer.reverse = node
    traverse(head)
    return

def deletion(head,index):
    print("The Updated Double Linked List is: ")
    pointer = head
    count = 0

    if(index == 0):
        pointer = pointer.next
        pointer.reverse = None
        head = pointer
        traverse(head)
        return
    
    while pointer and count < index -1:
        pointer = pointer.next
        count = count+1
    
    temp1 = pointer.next

    if (temp1.next == None):
        pointer.next = None
        temp1.reverse = None
        traverse(head)
        return

    
    temp2 = temp1.next
    pointer.next = temp1.next
    temp2.reverse = pointer
    traverse(head)
    return


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node2.reverse = node1
node3.reverse = node2
node4.reverse = node3
node5.reverse = node4

traverse(node1)
insertion(node1,5,5)
deletion(node1,4)