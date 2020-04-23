def palindrome (stringy):
    a = len(stringy)%2
    str = sorted(stringy)
    b = True
    if(a==0):
        for i in range(1, len(str), 2):
            if str[i] != str[i-1]:
                b = False
                break
    one_chance = False
    if(a==1):
        for i in range(1, len(str), 2):
            if (str[i] != str[i-1])and one_chance:
                b=False
                break
            elif str[i] != str[i-1]:
                one_chance = True
    return b


print(palindrome("nana"))