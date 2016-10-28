
n = int(input().strip())
num_hash = 1
num_space = n-1
while num_space >= 0:
  print(num_space*' '+num_hash*'#')
  num_space -= 1
  num_hash += 1
