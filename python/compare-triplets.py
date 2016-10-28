a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

arr = [a0,a1,a2,b0,b1,b2]
bob_tot = 0
alice_tot = 0
i = 0

while i < 3: 
  if arr[i] > arr[i+3]:
    alice_tot += 1
    i+=1
  elif arr[i] < arr[i+3]:
    bob_tot += 1
    i+=1
  else: 
    i+=1

print (str(alice_tot) + " " + str(bob_tot))
