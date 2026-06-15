class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in count_map.items():
            buckets[count].append(num)
        
        print(buckets)
        
        result = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                if len(result)<k:
                    result.append(num)

        return result
