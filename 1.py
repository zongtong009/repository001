>>> ord('孙⁢')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ord('孙⁢')
TypeError: ord() expected a character, but string of length 2 found
>>> ord('⁢')
8290
>>> chr(8290)
'\u2062'
