from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = Counter(s)
        freq2 = Counter(t)

        if len(s) != len(t):
            return False

        for char in s:
            if freq1[char] != freq2[char]:
                return False
        
        return True

        