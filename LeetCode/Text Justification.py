# coding:utf-8
# created by Phoebe_px on 2017/3/23
'''
Description:
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

problem-solving ideas:
key points: 'temp' to record <maxWidth words
            'num_of_letters' to record <maxWidth letters's numbers in words

'''
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result,temp,num_of_letters=[],[],0
        for w in words:
            if num_of_letters+len(temp)+len(w)>maxWidth:
                for i in range(maxWidth-num_of_letters):
                    #to average and add blank
                    temp[i%(len(temp)-1) or 1]+=' '
                result.append(''.join(temp))
                temp,num_of_letters=[],0
            temp+=[w]
            num_of_letters+=len(w)
        return result+[' '.join(temp).ljust(maxWidth)]
#test
a = Solution()
print(a.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))