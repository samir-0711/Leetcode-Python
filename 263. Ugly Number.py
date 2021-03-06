"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""
"""
Algorithm:
Just divide by 2, 3 and 5 as often as possible and then check whether we arrived at 1
"""
"""
@param {int} num
@return {bool}
"""
def isUgly(num):
    if num <= 0:
        return False
    for i in [2, 3, 5]:
        while num % i == 0:
            num /= i
    return num == 1
