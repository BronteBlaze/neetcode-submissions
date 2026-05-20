class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {} 
        dictT = {}
        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i], 0) + 1
        for i in range(len(t)):
            dictT[t[i]] = dictT.get(t[i], 0) + 1
        if dictS==dictT:
            return True
        return False
