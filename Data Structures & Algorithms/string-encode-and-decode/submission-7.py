class Solution:

    def encode(self, strs: List[str]) -> str:
        # length#stringlength#string
        encoded = ""
        for word in strs:
            encoded += (str(len(word))+'#'+word)
        return encoded

    def decode(self, s: str) -> List[str]:
        # 12#aadadadadada5#world
        i=0

        result = []

        j=i
        while j<len(s):

            if s[j]=='#':
                length = int(s[i:j])
                word_start_index = j+1
                word_end_index = word_start_index+length
                word = s[word_start_index:word_end_index]

                result.append(word)

                j=word_end_index
                i=j
            else:
                j+=1
        
        print(result)
        
        return result

