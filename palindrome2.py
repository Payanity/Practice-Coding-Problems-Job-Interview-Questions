import sys
def palindromeIt(n,times):
  stringy = ""
  r=list(reversed(str(n)))
  for i in r:
      stringy += i
  reverseN = int(stringy)
  addedN = n + reverseN
  print(addedN)
  stringer = ""
  rAdded = list(reversed(str(addedN)))
  for j in rAdded :
    stringer += j
  reverseAddedN = int(stringer)
  if (addedN != reverseAddedN):
     return palindromeIt(addedN, times+1)
  return times, addedN

for line in sys.stdin:
    num = int(line)
    print(palindromeIt(num,1))