# coding:utf-8
# created by Phoebe_px on 2017/3/21
'''
Description:
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
You need to return the number of important reverse pairs in the given array.
Example1:
Input: [1,3,2,3,1]
Output: 2
Example2:
Input: [2,4,3,5,1]
Output: 3

Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.

problem-solving ideas:
Solution1: FenwickTree
Solution2: MergeSort
Solution3: bisect

'''
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
class Solution1(object):
    def reversePairs(self, nums):
        nums2=[2*x for x in nums]
        temp = {v:k+1 for k,v in enumerate(sorted(set(nums+nums2)))}
        ft = FenwickTree(len(temp))
        result = 0
        for i in nums2[::-1]:
            result+=ft.sum(temp[i//2]-1)
            ft.add(temp[i],1)
        return result


class Solution2(object):
    def __init__(self):
        self.count=0
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def msort(nums):
            l = len(nums)
            if l<=1: return nums
            else:
                return merge(msort(nums[:l//2]),msort(nums[l//2:]))
        def merge(left,right):
            l,r = 0,0
            while l<len(left) and r<len(right):
                if left[l]<=2*right[r]:
                    l+=1
                else:
                    self.count+=len(left)-l
                    r+=1
            return sorted(left+right)
        msort(nums)
        return self.count

import bisect
class Solution3(object):
    def reversePairs( self,nums):
        count = 0
        done = []
        for num in nums:
            count += len(done) - bisect.bisect(done, num * 2)
            bisect.insort(done, num)
        return count

#Test
a = Solution1()
b = Solution2()
c = Solution3()
print(a.reversePairs([1,3,2,3,1]))  # 2
print(a.reversePairs([2,4,3,5,1]))  # 3
print(b.reversePairs([1,3,2,3,1]))  # 2
print(b.reversePairs([2,4,3,5,1]))  # 3
print(c.reversePairs([1,3,2,3,1]))  # 2
print(c.reversePairs([2,4,3,5,1]))  # 3