# coding:utf-8
# created by Phoebe_px on 2017/3/3
'''
Description:
two non-empty linked lists representing two non-negative integers
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
for example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 8 -> 0 -> 7
'''
class listnode():
    def __init__(self,x):
        self.val = x
        self.next = None
class linklist():
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def initlist(self,data):
        self.head = listnode(data[0])
        p = self.head
        for i in data[1:]:
            p.next = listnode(i)
            p = p.next
    def preappend(self,elem):
        if self.head is None:
            self.head=listnode(elem)
        else:
            p = listnode(elem)
            p.next = self.head
            self.head = p
    def pop(self):
        if self.head :
            elem = self.head.val
            self.head = self.head.next
            return elem
        else:
            raise UnboundLocalError
    def length(self):
        len=0
        p = self.head
        while p :
            len+=1
            p = p.next
        return len
    def printlist(self):
        temp = ''
        p = self.head
        while p :
            temp += str(p.val)+' '
            p = p.next
        return temp

class solution():
    def addTwoNumbers(self,a,b):
        value =linklist()
        flag = 0
        p = a.head
        q = b.head
        while p or q or flag:
            v1 = v2 = 0
            if p:
                v1 = p.val
                p = p.next
            if q:
                v2 = q.val
                q = q.next
            flag,m = divmod(v1+v2+flag,10)
            value.preappend(m)
        return value
## test correct
a = linklist()
a.initlist([2,4,3])
b = linklist()
b.initlist([5,6,4])
m = solution()
result = m.addTwoNumbers(a,b)
print(result.printlist())



