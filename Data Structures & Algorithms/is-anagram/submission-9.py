class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ch = [0] * 26

        for l in s:
            ch[ord('a')-ord(l)] += 1

        for b in t:
            ch[ord('a')-ord(b)] -= 1

        return all(i==0 for i in ch) 
    
