class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        ans = dict()
        for i in range(len(s)):
            ans[s[i]] = ans.get(s[i], 0) + 1
            ans[t[i]] = ans.get(t[i], 0) - 1
        
        for value in ans.values():
            if value!=0:
                return False
        
        return True