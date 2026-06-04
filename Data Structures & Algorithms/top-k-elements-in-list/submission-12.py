class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)

        heap = []

        for num, count in count_map.items():
            heapq.heappush(heap, (count, num))

            if len(heap)>k:
                heapq.heappop(heap)


        return [num for count, num in heap]     