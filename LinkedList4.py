class Node:
    def __init__(self,value):
        self.value = value
        self.next= None
class LinkedList:
    def __init__(self, head):
        self.head = head

def delNode(n):
    if(n.next == None):
        n=None
    else:
        n.value=n.next.value
        n.next = n.next.next

a=Node(5)
b=Node(3)
c=Node(1)
a.next=b
b.next=c
d=LinkedList(a)
delNode(c)
while d.head!=None:
    print(d.head.value)
    d.head = d.head.next