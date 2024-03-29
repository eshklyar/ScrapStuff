class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        result = []
        stack = []
        for char in s:
            if char.lower() in vowels:
                result.append(None)
                stack.append(char)
            else:
                result.append(char)
        
        # for char in result:
        #     if char == None:
        #         result[result.index(char)] = stack.pop()

        for i, char in enumerate(result):
            if char == None:
                result[i] = stack.pop()

        return "".join(result)

s = Solution()
# print(s.reverseVowels("hello"))
# print(s.reverseVowels("leetcode"))
# print(s.reverseVowels("aA"))
# print(s.reverseVowels("0A"))
with open("text") as f:
    t = f.read()
# print(t)
print(s.reverseVowels(t))