# coding:utf-8
# created by Phoebe_px on 2017/3/12
'''
Description:
Determine whether an integer is a palindrome. Do this without extra space.

problem-solving ideas:
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x!=0 and x%10==0) :
            return False
        c,h=x,1
        #get x's digits
        while c/h>=10:
            h *=10

        while c > 0:
            # judge x's last number and x's first number
            if c/h != c%10 : return False
            # go head to tail
            c = c%h
            c= c/10
            print(c)
            h = h/100
        return True

#test
a = Solution()
print(a.isPalindrome(-5))   # False
print(a.isPalindrome(121))  # True