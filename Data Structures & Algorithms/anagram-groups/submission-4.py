class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_map = defaultdict(list)

        for st in strs:
            st_table = [0] * 26

            for ch in st:
                st_table[ord(ch)-ord('a')] += 1

            tup_table = tuple(st_table)
            
            anag_map[tup_table].append(st)

        return list(anag_map.values())

            