class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)

        for num in nums:
            if num in count_map:
                count_map[num]+=1
            else:
                count_map[num]=1
        
        sorted_count_map = dict(sorted(count_map.items(), key=lambda item: item[1], reverse=True))
        print(sorted_count_map)

        return list(sorted_count_map.keys())[:k]
