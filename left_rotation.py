def array_left_rotation(a, n, k):
  i = 0
  new_a = []
  new_a.extend(a)
  while i < n: 
      new_ind = i - k
      new_a[new_ind] = a[i]
      i += 1
  return new_a
      
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')