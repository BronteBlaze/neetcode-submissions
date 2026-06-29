class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        stack=[]
        result=[0]*n
        for i in range(n):
            j=len(stack)-1
            while j>=0:
                if temperatures[i]>temperatures[stack[j]]:     
                    day=i-stack[j]
                    result[stack[j]]=day
                    stack.pop()
                j-=1
            stack.append(i)
        
        return result
