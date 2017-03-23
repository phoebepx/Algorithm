# coding:utf-8
# created by Phoebe_px on 2017/3/22
'''
Description:
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:
Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

problem-solving ideas:

method1 : FenwickTree
method2 : MergeSort

'''
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #去重+排序
        insort={}
        for k,v in enumerate(sorted(set(nums))):
            insort[v]=k+1
        snums = [insort[x] for x in nums]
        result = [0]*len(nums)
        ft = FenwickTree(len(nums))
        for i in range(len(snums)-1,-1,-1):
            result[i]=ft.sum(snums[i]-1)    #求出第snums[i]排位的逆序数
            ft.add(snums[i],1)              #将其加入树状数组
        return result

class FenwickTree(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n + 1)

    def add(self, x, val):
        while x <= self.n:
            self.sums[x] += val
            x += self.lowbit(x)


    def lowbit(self, x):
        return x & -x

    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sums[x]
            x -= self.lowbit(x)
        return res

class Solution_mergesort(object):
    def countSmaller(self,nums):
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
#test
a = Solution()
b = Solution_mergesort()
print(a.countSmaller([5,2,6,1]))    #[2,1,1,0]
print(b.countSmaller([5,2,6,1]))    #[2,1,1,0]