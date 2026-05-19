class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_list = [ord(char) for char in s]
        sum = 0
        for i in range(len(ascii_list)):
                if i==len(ascii_list)-1:
                    break
                else:
                    difference = abs(ascii_list[i+1]-ascii_list[i])
                sum += difference
        return sum