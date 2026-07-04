class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        count_fleet_stack = []
        for p, s in cars:
            t = (target - p)/s
            if not count_fleet_stack or t>count_fleet_stack[-1]:
                    count_fleet_stack.append(t)
        
        return len(count_fleet_stack)