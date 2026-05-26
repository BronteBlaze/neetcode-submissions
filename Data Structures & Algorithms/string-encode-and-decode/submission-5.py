class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += (str(len(word))+"#"+word)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0

        decoded_string = []
        while i<len(s):
            j=i
            
            while s[j]!="#":
                j+=1

            end_length = j-1
            if i==end_length:
                length = int(s[i])
            else:
                length = s[i:end_length+1]
                length = int(length)

            start_index = j+1
            end_index = start_index + length
    
            decoded = s[start_index:end_index]
            decoded_string.append(decoded)
            
            i=end_index

        return decoded_string

