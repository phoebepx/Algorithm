# coding:utf-8
# created by Phoebe_px on 2017/3/9
'''
Description:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

'''

'''
problem-solving ideas:
1、Brute force method: Solution1
2、easy method: Solution2 (from middle to two ends)
'''

class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        palinmax = ''
        l = list(s)
        Palind = []
        for i in range(len(l)):
            for j in range(i,len(l)):
                Palind.append(l[j])
                if self.isPalindrome(("".join(Palind))) and len(Palind) > maxlen:
                    maxlen = len(Palind)
                    palinmax = ("".join(Palind))
            Palind = []
        return palinmax
    def isPalindrome(self,s):
        l = list(s)
        l.reverse()
        l=("".join(l))
        return l == s
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxpalind = ''
        for i in range(len(s)):
            temp = self.get_longest_palindrome(s,i,i)
            if len(temp)>len(maxpalind):
                maxpalind = temp
            temp = self.get_longest_palindrome(s,i,i+1)
            if len(temp)>len(maxpalind):
                maxpalind = temp
        return maxpalind
    def get_longest_palindrome(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1;r+=1
        return s[l+1:r]

#test
a = Solution2()
print(a.longestPalindrome('babad'))
