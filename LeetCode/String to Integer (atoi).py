# coding:utf-8
# created by Phoebe_px on 2017/3/11
'''
Description:
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
what are the possible input cases.

problem-solving ideas:
method1
covert str to list and use function isdigit(),ord()
refer to myAtoi1()

method2
use re.findall() to do string matching
refer to myAtoi2()
'''

import re
class Solution(object):
    def myAtoi1(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str)==0: return 0
        l = list(str.strip())
        flag = -1 if l[0]=='-' else 1
        if l[0] in ['+','-','0']: del l[0]
        result,i = 0,0
        while i <len(l) and l[i].isdigit():
            result = result*10+ord(l[i])-ord('0')
            i+=1
        return min(max(-2**31,flag*result),2**31-1)
    def myAtoi2(self, str):
        if len(str)==0: return 0
        str = re.findall('^[\+\-0]*\d+',str.strip())
        try:
            result = int(''.join(str))
            return min(max(-2**31,result),2**31-1)
        except:
            return 0

#test method1
a = Solution()
print(a.myAtoi1('i123')) #0
print(a.myAtoi1('-123')) #-123
print(a.myAtoi1('0123')) #123
print(a.myAtoi1('123i')) #123
#test method2
print(a.myAtoi2('i123')) #0
print(a.myAtoi2('-123')) #-123
print(a.myAtoi2('0123')) #123
print(a.myAtoi2('123i')) #123
