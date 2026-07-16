class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        left = 0

        time_key = self.time_map[key]

        right = len(time_key)-1

        answer=""
        while left<=right:
            med = (left+right)//2

            if time_key[med][0]<=timestamp:
                answer=time_key[med][1]
                left=med+1
            else:
                right=med-1
        
        return answer
