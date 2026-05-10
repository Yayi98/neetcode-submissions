from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        mydict = {'(': ')', '{': '}', '[':']'}
        for char in list(s):
            if len(mystack) > 0 and mystack[-1] in mydict and mydict[mystack[-1]] == char:
                del mystack[-1]
            else:
                mystack.append(char)
        return len(mystack) == 0