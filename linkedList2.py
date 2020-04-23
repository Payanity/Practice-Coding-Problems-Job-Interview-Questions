class Node:
    def __init__(self, value):
        self.data=value
        self.next = None
class LinkedList:
    def __init__(self, head):
        self.head = head

def deleteDup(listt):
    list = []
    h=listt.head
    previous = None
    while(listt.head != None):
        if(listt.head.data in list):
            previous.next = listt.head.next
        else:
            list.append(listt.head.data)
            previous = listt.head
        listt.head = listt.head.next
    return h
a = Node(5)
b = Node(5)
c = Node(1)
d = LinkedList(a)
a.next=b
b.next=c

f=deleteDup(d)

while f:
    print(f.data)
    f=f.next





