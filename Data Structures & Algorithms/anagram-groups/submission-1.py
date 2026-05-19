class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for s in str:
                count[ord(s) - ord('a')] += 1
            strs_dict[tuple(count)].append(str)
        
        return list(strs_dict.values())