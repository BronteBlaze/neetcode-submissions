class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operators:
                operand.append(token)
            
            else:
                last = int(operand.pop())
                second_last = int(operand.pop())

                if token=="+":
                    operand.append(second_last+last)
                elif token=="-":
                    operand.append(second_last-last)
                elif token=="*":
                    operand.append(second_last*last)
                else:
                    operand.append(second_last/last)
        
        return int(operand[0])