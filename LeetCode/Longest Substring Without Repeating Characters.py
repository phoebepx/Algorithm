# coding:utf-8
# created by Phoebe_px on 2017/3/6
'''
Description:
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        allstr = list(s)
        substr = []
        maxl = 0
        start = 0
        for i in range(len(s)):
            if allstr[i] in substr:
                start = substr.index(allstr[i])+1
                substr = substr[start:]
                substr.append(allstr[i])
            else:
                substr.append(allstr[i])
            maxl = max(len(substr),maxl)
        return maxl

#test
a = Solution()
print(a.lengthOfLongestSubstring('abcabcbb'))
print(a.lengthOfLongestSubstring('bbbb'))