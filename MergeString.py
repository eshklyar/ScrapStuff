class Solution:
    def __init__(self, solution):
        self.solution = solution
    def mergeAlternately(self, word1: str, word2: str) -> str:
        solutionString = ""
        if len(word1) == len(word2):
            for i, j in zip(word1, word2):
                solutionString += i+j
            # num = 0
        else:
            if len(word1) > len(word2):
                for i, j in zip(word1[:len(word2)], word2):
                    solutionString += i + j
                solutionString += word1[len(word2):len(word1)]
            else:
                for i, j in zip(word1, word2[:len(word1)]):
                    solutionString += i + j
                solutionString += word2[len(word1):len(word2)]

        # print(solutionString)
        return solutionString


x = Solution("")
x.solution = x.mergeAlternately("abcde", "1235678")
print(x.solution)