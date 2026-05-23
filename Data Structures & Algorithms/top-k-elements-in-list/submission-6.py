class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        sorted_count_map = dict(sorted(count_map.items(), key=lambda x: x[1], reverse=True))
        print(sorted_count_map)

        keys = [key for i, key in enumerate(sorted_count_map.keys()) if i<k]

        return keys