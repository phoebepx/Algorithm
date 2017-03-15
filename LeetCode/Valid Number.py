# coding:utf-8
# created by Phoebe_px on 2017/3/13
'''
Description:
Validate if a given string is numeric.
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

problem-solving ideas:
key point: DFA
'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define DFA
        state = [{},
              {'blank': 1, 'sign': 2, 'digit':3, '.':4},
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
        currentState = 1

        for i in s:
            if i >='0' and i<='9':
                i = 'digit'
            if i in ['+','-']:
                i = 'sign'
            if i ==' ' :
                i = 'blank'
            if i not in state[currentState].keys():
                return False
            currentState = state[currentState][i]
            if currentState not in [3,5,8,9]:
                return False
            return True

#test
a = Solution()
print(a.isNumber('.e-1'))   #False
print(a.isNumber('e2'))     #False
print(a.isNumber('2e10'))   #True


