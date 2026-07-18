class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0 
        p2 = len(s) - 1

        while(p1 <  p2):

            #Adding not in front of it means: 
            #"Give me True if the character is NOT a letter or a number."
            while p1<p2 and not s[p1].isalnum():
                p1+=1
            while p1<p2 and not s[p2].isalnum():
                p2-=1
            if s[p1].lower() != s[p2].lower():
                return False
            p1+=1
            p2-=1
        return True