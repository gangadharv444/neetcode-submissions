class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        string = ""

        for i in range(n):
            s = strs[i]
            for j in range(len(s)):
                string += str(ord(s[j]))
                string += '#'

            string += '|'
        
        return string


    def decode(self, s: str) -> list[str]:
    
        if not s:
            return []
            
        decoded_strs = []
        
        
        words = s.split('|')[:-1] 
        
        for word in words:
            current_word = ""
            
            
            ascii_values = word.split('#')[:-1]
            
            for val in ascii_values:
                
                current_word += chr(int(val))
                
            decoded_strs.append(current_word)
            
        return decoded_strs

























