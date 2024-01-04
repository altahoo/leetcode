# 271. Encode and Decode Strings

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# You are not allowed to solve the problem using any serialize methods (such as eval).


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ''
        for s in strs:
            encoded_string += s.replace('/', '//') + '/:'
        
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strings = []
        current_string = ''
        i = 0

        while i < len(s):
            if s[i:i+2] == '//':
                current_string += '/'
                i += 2
            elif s[i:i+1] == '/':
                decoded_strings.append(current_string)
                current_string = ''
                i += 2
            else:
                current_string += s[i]
                i += 1
        return decoded_strings
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))