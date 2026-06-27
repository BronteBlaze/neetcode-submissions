class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for bracket in s:
            if bracket in bracket_map.values():
                open_brackets.append(bracket)
            else:
                if not open_brackets or bracket_map[bracket]!=open_brackets[-1]:
                    return False
                
                open_brackets.pop()
        
        return len(open_brackets)==0

