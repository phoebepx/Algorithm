# coding:utf-8
# created by Phoebe_px on 2017/3/8
'''
Description:
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
Example :
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
'''

'''
problem-solving ideas:
be similar to the probelm of find_kth_nums , first to realize find_kth_nums ,
if sum length of nums1 and nums2 is odd , to take the middle number;
else take avg of middle two numbers.

find_kth_nums:
4 kinds of status:
k < sum of a and b's median indices
    a's median < b's median

'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1)+len(nums2)
        if l%2 ==1:
            return self.find_kth_nums(nums1,nums2,l//2)
        else:
            return (self.find_kth_nums(nums1,nums2,l//2-1)+self.find_kth_nums(nums1,nums2,l//2))/2.0

    def find_kth_nums(self,A,B,k):
        if not A:
            return B[k]
        if not B:
            return A[k]
        ia = len(A)//2
        ib = len(B)//2
        na = A[ia]
        nb = B[ib]
        # when k is bigger than the sum of a and b's median indices
        if ia+ib<k :
            if na<nb:   # if b's median is bigger than a's, a's first half doesn't include k
                return self.find_kth_nums(A[ia+1:],B,k-ia-1)
            else:
                return self.find_kth_nums(A,B[ib+1:],k-ib-1)
        # when k is smaller than the sum of a and b's median indices
        else:
            if na<nb:  # if b's median is bigger than a's, b's second half doesn't include k
                return self.find_kth_nums(A,B[:ib],k)
            else:
                return self.find_kth_nums(A[:ia],B,k)
#test
A = [5,6,7]
B = [1,2,3,4,5]
a = Solution()
print(a.findMedianSortedArrays(A,B))  # 4.5
