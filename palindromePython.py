def isPalindrome(x):
    a = True
    b = str(x)
    for i in range(0, int((len(b) / 2))):
        if b[i] != b[len(b) - i - 1]:
            a = False
            break
    return a

print(isPalindrome(10011))

def isPalindr(x):
    return str(x)==str(x)[::-1]

print(isPalindr(1001))