# coding:utf-8
# created by Phoebe_px on 2017/3/16
'''
Description:
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,
Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]


problem-solving ideas:

key point: BFS

'''
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if beginWord==endWord:
            return [[beginWord]]
        graph = {}     #create a graph dict, vertex represent word ,edge represent that this two vertex are only one letter different
        result = []    #record all paths from beginWord to endWord
        graph[beginWord]=self.Only_1_letter(beginWord,wordList)
        #init beginWord  neighbour
        for s in wordList:
            graph[s]=self.Only_1_letter(s,wordList)
        #use queue def BFS
        queue = [(beginWord,[beginWord])]
        while queue:
            vertex,path = queue.pop(0)
            for next in graph[vertex]-set(path):
                if next==endWord:
                    result.append(path+[next])
                else:
                    queue.append((next,path+[next]))
        #based on all paths to find the shortest path ,record in final_r
        final_r = []
        min = len(result[0])
        for i in range(len(result)):
            if len(result[i])<=min:
                final_r.append(result[i])
        return final_r
    #judge str1,str2 whether only one letter difference
    def diff_of_str(self,str1,str2):
        count = 0
        l1=list(str1);l2=list(str2)
        for i in range(len(l1)):
            if l1[i]!=l2[i]:
                count+=1
        return count == 1
    # in wordList ,candidate set is a list with str only one letter difference
    def Only_1_letter(self,str,wordlist):
        candidate = set()
        for s in wordlist:
            if self.diff_of_str(str,s):
                candidate.add(s)
        return candidate
#Test
a = Solution()
print(a.findLadders('hit','cog',["hot","dot","dog","lot","log","cog"]))
#[['hit', 'hot', 'lot', 'log', 'cog'], ['hit', 'hot', 'dot', 'dog', 'cog']]

