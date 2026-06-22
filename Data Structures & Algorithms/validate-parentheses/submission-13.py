class Solution:
    def isValid(self, s: str) -> bool:
        close_order = []

        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']

        bracket_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        n = len(s)

        count=0

        if n<=1:
            return False
        
        if all(ch in open_brackets for ch in s) or all(ch in close_brackets for ch in s):
            return False

        for i in range(n):
            if s[i] in open_brackets:
                close_order.append(s[i])
            if s[i] in close_brackets:
               if len(close_order)==0:
                 return False
               length = len(close_order)
               last = close_order[length-1]


               if bracket_map[last]==s[i]:
                   print(s[i])
                   count+=2
                   close_order.pop()

        print(count)
        
        return count==n