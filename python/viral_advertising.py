n = int(input())
num_shared = 5
total = 0

for num in range(n):
    num_liked = int(num_shared/2)
    total += num_liked
    num_shared = num_liked*3

print(total)  
