class LinkedListNode1:
    def __init__(self, data):
        self.dataval = data
        self.next = None
class LinkedList:
    def __init__(self,h):
        self.head = h

class Index:
    value = 0




def kth_to_last1(head, k):
    i = Index()
    return kth_to_last(head, k, i)

def kth_to_last(head, k, idx):
    if (head == None):
        return None
    index = kth_to_last(head.next, k, idx)
    idx.value = idx.value+1
    if(idx.value==k):
        return head
    return index


#is this supposed to be an iter bc node is one in front??? How?????


b = LinkedListNode1(4)
c = LinkedListNode1(5)
d = LinkedListNode1(6)
e = LinkedListNode1(7)
l = LinkedList(b)

b.next = c
c.next = d
d.next = e
g=kth_to_last1(b,3)
print(g.dataval)




