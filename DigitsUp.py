def plusOne(digits, num):
    #9999999, tooo
    if(digits[len(digits)-1-num] == 9):
        digits[len(digits) - 1 - num] = 0
        if(num == len(digits)-1):
            digits.insert(0,1)
            return digits
        else:
            num+=1
            return plusOne(digits, num)
    else:
        digits[len(digits)-1-num]+=1
        return digits


k=[9,9,9,9,9,8,9]
print(plusOne(k,0))