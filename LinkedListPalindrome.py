# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
             self.val = x
             self.next = None
def isPalindrome(head):
    list = []
    while(head != None):
        list.append(head.val)
        head = head.next
    a = 0
    half = int(len(list)/2)
    while len(list) > half+1:
        print(list)
        if (list[a] != list.pop()) and (len(list)>1):
            return False
        a+=1
    return True

b = ListNode(2)
c = ListNode(2)
d = ListNode(3)
e = ListNode(3)
f = ListNode(1)
g= ListNode(2)
h = ListNode(2)

b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

print(isPalindrome(b))
