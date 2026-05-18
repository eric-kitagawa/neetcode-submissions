class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = []
        for s in strs:
            n = len(s)
            encoded = f"{n}#{s}"
            encoded_strs.append(encoded)
        
        result = "".join(encoded_strs)

        return result


    def decode(self, s: str) -> List[str]:
        if not s: 
            return []
        
        if len(s) < 3:
            return [""]

        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])

            i = j
        
        return decoded



