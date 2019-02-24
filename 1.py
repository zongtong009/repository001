>>> ord('孙⁢')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ord('孙⁢')
TypeError: ord() expected a character, but string of length 2 found
>>> ord('⁢')
8290
>>> chr(8290)
'\u2062'
s=[1,5,12,6,78,24]
def fun(s):
    result = 0
    for i in s:
        if s[i] in s.pop(i):
            result = 1
    return result