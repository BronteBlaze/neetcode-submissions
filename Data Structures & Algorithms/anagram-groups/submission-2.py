class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for str in strs:
            sorted_str = ''.join(sorted(str))
            anagram_map[sorted_str].append(str)
        return [value for value in anagram_map.values()]
            