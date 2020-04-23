class Node:
    def __init__(self,value):
        self.value = value
        self.next= None
class LinkedList:
    def __init__(self, head):
        self.head = head

def delDup(list):
    current = list.head
    while(current!=None):
        iter = current
        while(iter.next!= None):
            if(iter.next.value==current.value):
                iter.next = iter.next.next
            else:
                iter = iter.next
        current = current.next

a = Node(3)
b = Node(2)
c = Node(3)
d = Node(2)
e = Node(4)


a.next=b
b.next=c
c.next=d
d.next=e
z = LinkedList(a)

delDup(z)

while z:
    print(z.head.value)
    z.head = z.head.next