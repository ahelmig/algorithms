#!/bin/python3

import sys
import re

s_len = int(input().strip())
s = input().strip()
i, max_len = 0, 0
letters = ''.join(set(s))

if s_len <= 2: 
  if len(letters) < 2:
    max_len = 0
  else:
    max_len = len(s)
else: 
  while i != len(letters):
    temp1 = letters[i]
    j = i + 1
    while j != len(letters):
      temp2 = letters[j]
      t = ''
      for char in s:
        if char == temp1:
          t += char
        elif char == temp2:
          t += char
        else:
          t += ''
      regex = re.compile(r'(\w)\1')
      match = regex.search(t)
      if match:
        max_len = max_len
      else: 
        length = len(t)
        if length > max_len:
          max_len = length
        else:
          max_len = max_len
      j += 1
    i += 1

print (str(max_len))