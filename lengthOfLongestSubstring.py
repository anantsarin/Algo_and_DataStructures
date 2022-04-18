# lengthOfLongestSubstring.py

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lls = 0
        sub = ''
        for c in s:
            if c not in sub:
                sub = sub +c
                lls = max(lls, len(sub))
            else:
                cut_till =  sub.index(c)
                sub = sub[cut_till+1:] + c

        return lls
