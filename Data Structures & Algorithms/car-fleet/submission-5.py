class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ptime_map = defaultdict(int)

        n = len(position)
        for i in range(n):
            time = (target - position[i])/speed[i]
            ptime_map[position[i]] = time

        ptime_map = dict(sorted(ptime_map.items(), key=lambda x: x[0], reverse=True))
        
        count_fleet_stack = []
        for t in ptime_map.values():
            if not count_fleet_stack or t>count_fleet_stack[-1]:
                    count_fleet_stack.append(t)
        
        return len(count_fleet_stack)