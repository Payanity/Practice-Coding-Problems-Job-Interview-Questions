import math
def letterCombinations(digits):
    dict = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g","h","i"], 5:["j", "k", "l"],
            6 : ["m", "n", "o"], 7 : ["p", "q", "r", "s"], 8: ["t", "u","v"], 9: ["w", "x", "y", "z"]}
    array = [""] * pow(3, len(digits))
    time = 0
    while time < len(array):
        if(int(digits[k])!= 9):
            array[0+ time] += (dict[int(digits[k])][0])
            array[1+ time] += (dict[int(digits[k])][1])
            array[2+ time] += (dict[int(digits[k])][2])
            time+=3



arr= []
letterCombinations("23", arr)
print(arr)

class Solution:
    array =[]
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        dict = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g","h","i"], 5: ["j", "k", "l"], 6 : ["m", "n", "o"], 7 : ["p", "q", "r", "s"], 8: ["t", "u",          "v"], 9: ["w", "x", "y", "z"]}
        for i in dict[int(digits[0])]:
                 if (len(digits)<=1):
                        return i
                 else:
                        stringy = i + letterCombinations(digits[1:])
                        #return array