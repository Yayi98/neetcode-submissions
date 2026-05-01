class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set, t_set = {}, {}
        if len(s) != len(t):
            return False
        for i, j in zip(s, t):
            if i in s_set:
                s_set[i] += 1
            else:
                s_set[i] = 1
            if j in t_set:
                t_set[j] += 1
            else:
                t_set[j] = 1
        if s_set == t_set:
            return True
        else:
            return False