import math

class Solution:
    def reverse(self, x: 'int') -> 'int':
        a = str(x)[::-1]
        if a[len(a) - 1] == "-":
            a = "-" + a[0:len(a) - 1]
        if (int(a) >= pow(2, 31)):
            return 0
        elif (int(a) < -pow(2, 31)):
            return 0
        return int(a)
