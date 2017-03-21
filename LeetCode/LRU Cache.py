# coding:utf-8
# created by Phoebe_px on 2017/3/21
'''
Description:
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ )
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       // returns 1
cache.put(3, 3)    // evicts key 2
cache.get(2)       // returns -1 (not found)
cache.put(4, 4)    // evicts key 1
cache.get(1)       // returns -1 (not found)
cache.get(3)       // returns 3
cache.get(4)       // returns 4

problem-solving ideas:
key points:
method1: OrderedDict()
method2: double linked list
'''
#method1: OrderedDict()
from collections import OrderedDict
class LRUCache1(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if  key not in self.cache.keys():
            return -1
        else:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache.keys():
            self.cache.pop(key)
        elif self.capacity==len(self.cache):
            self.cache.popitem(last = False)
        self.cache[key]=value
#method2: double linked list
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.pre=None
        self.next=None


class LRUCache2(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.data={}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next=self.tail
        self.tail.pre=self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.data.keys():
            n = self.data[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.data.keys():
            self._remove(self.data[key])
        elif len(self.data)==self.capacity:
            n = self.head.next
            self._remove(n)
            del self.data[n.key]
        n = Node(key,value)
        self.data[key]=n
        self._add(n)

    def _remove(self,node):
        p = node.pre
        n = node.next
        p.next=n
        n.pre=p
    def _add(self,node):
        p=self.tail.pre
        p.next=node
        node.pre = p
        node.next = self.tail
        self.tail.pre = node
#test
cache = LRUCache2(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))         #returns 1
cache.put(3, 3)             #evicts key 2
print(cache.get(2))         # returns -1 (not found)
cache.put(4, 4)             # evicts key 1
print(cache.get(1))         # returns -1 (not found)
print(cache.get(3))         # returns 3
print(cache.get(4))         #return 4

