class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.reverse = None

def traverse(head):
    pointer = head
    print(pointer.data,end="<-->")
    pointer = pointer.next
    while (pointer != head):
        print(pointer.data,end="<-->")
        pointer = pointer.next
    print(head.data)

def insertion(head,data,index):
    print("The Updated Double Circular List is: ")
    pointer = head
    node = Node(data)
    count = 0

    if (index == 0):
        head.reverse.next = node
        node.reverse = head.reverse
        node.next = pointer
        pointer.reverse = node
        head = node
        traverse(head)
        return

    while pointer and count < index-1:
        pointer = pointer.next
        count = count +1
    
    node.next = pointer.next
    pointer.next = node
    pointer.next.reverse = node
    node.reverse = pointer
    traverse(head)
    return

def deletion(head,index):
    print("The Updated Double Circular List is: ")
    pointer = head
    count = 0

    if (index == 0):
        pointer = pointer.next
        head.reverse.next = pointer
        pointer.reverse = head.reverse
        head = pointer
        traverse(head)
        return 

    while pointer and count < index-1:
        pointer = pointer.next
        count = count+1
    
    temp = pointer.next
    pointer.next = temp.next
    temp.next.reverse = pointer
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
node5.next = node1

node1.reverse = node5
node2.reverse = node1
node3.reverse = node2
node4.reverse = node3
node5.reverse = node4

head = node1

traverse(head)
insertion(head,100,0)
deletion(head,0)