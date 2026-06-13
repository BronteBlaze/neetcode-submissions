class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)

        heap = []

        for num, count in count_map.items():
            key = (count, num)

            heapq.heappush(heap, key)

            if len(heap)>k:
                heapq.heappop(heap)

        return [h[1] for h in heap]

