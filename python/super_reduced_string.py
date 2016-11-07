import re

S = input().strip()
pattern = re.compile(r'(\w)\1')
match = pattern.search(S)
while match:
  S = S.replace(match.group(), '')
  match = pattern.search(S)
print (S if S else 'Empty String')
