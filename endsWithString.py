def solution(text, ending):
  return text[-len(ending):] == ending



myS = "abcdefg"
endS = "efg"
print(solution(myS,endS))