class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for ch in s:
            if ch in bracket_map.values():
                stack.append(ch)
            else:
                if not stack or bracket_map[ch]!=stack[-1]:
                    return False
                
                stack.pop()
            
        return len(stack)==0