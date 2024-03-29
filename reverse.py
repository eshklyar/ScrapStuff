class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
    def revWords(self, s):
        # print(s.split())
        array = s.split()
        array.reverse()
        return " ".join(array)

    def reversedWords(self,s):
        return " ".join(reversed(s.split()))



s = Solution()
word = "edik is great"
# print(s.reverseWords(word))
# print(s.revWords(word))
print(s.reversedWords(word))