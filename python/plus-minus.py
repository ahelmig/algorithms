n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

num_pos, num_neg, num_zero = 0, 0, 0
for num in arr: 
  if num < 0: 
    num_neg += 1
  elif num > 0: 
    num_pos += 1
  else: 
    num_zero += 1

print (round(float(num_pos/n), 6))
print (round(float(num_neg/n), 6))
print (round(float(num_zero/n), 6))
