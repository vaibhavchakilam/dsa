class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverse(head):
    pointer = head.next
    print(head.data,end="-->")
    while pointer != head:
        print(pointer.data,end="-->")
        pointer = pointer.next
    print(head.data)
    print("The traversel of one Circular Linked List is complete")
    return

def insertion(head,data,index):
    print("The updated Circular list is: ")
    pointer = head
    node = Node(data)
    count = 0
    temp1 = pointer

    while temp1.next != head:
        temp1 = temp1.next

    if (index == 0):
        head = node
        head.next = pointer
        temp1.next = head
        traverse(head)
        return head

    while pointer and count< index-1:
        pointer = pointer.next
        count = count + 1
    
    if pointer.next is head:
        pointer.next = node
        node.next = head
        traverse(head)
        return head

    temp2 = pointer.next
    pointer.next = node
    node.next = temp2
    traverse(head)
    return head

def deletion(head,index):
    print("The updated Circular list is: ")
    pointer = head
    count = 0

    if (index == 0):
        pointer = pointer.next
        head = pointer
        traverse(head)
        return head

    while pointer and count < index-1:
        pointer = pointer.next
        count = count + 1
    
    temp = pointer.next
    pointer.next = temp.next
    traverse(head)
    return head

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
node3.next = node1

head = node1

traverse(head)
head = insertion(head,100,0)
head = deletion(head,0)