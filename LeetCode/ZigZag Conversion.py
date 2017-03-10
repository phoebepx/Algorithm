# coding:utf-8
# created by Phoebe_px on 2017/3/10
'''
Description:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

problem-solving ideas:
key point: set step to control the insert direction
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ['']*numRows
        step = (numRows==1)-1     #beginning step's value is 0 or -1
        index=0
        for x in s:
            if index == 0 or index == numRows-1:
                step =-step       #new round to change inserting direction
            result[index]+=x
            index+=step
        return ''.join(result)
#test
a = Solution()
print(a.convert('PAYPALISHIRING',3))  #PAHNAPLSIIGYIR