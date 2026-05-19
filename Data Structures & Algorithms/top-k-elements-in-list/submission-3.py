class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)

        for value in nums:
            nums_dict[value] += 1

        sorted_dict = dict(sorted(nums_dict.items(), key=lambda x: x[1], reverse=True))

        first_two_items =  list(sorted_dict.items())[:k]

        first_k_keys = [key for key, value in first_two_items]

        return first_k_keys