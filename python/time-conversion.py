time = input().strip()
new_time = ''

if time[8:10] == 'PM':
  if time[0:2] == '12':
    new_time += time[0:2]
  else:
    new_time += str(int(time[0:2])+12)
else:
  if time[0:2] == '12':
    new_time += '0'+ str(int(time[0:2])-12)
  else: 
    new_time += time[0:2]
new_time += time[2:6]
new_time += time[6:8]

print(new_time)
