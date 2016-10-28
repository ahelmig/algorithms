n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
sum1 = 0
sum2 = 0
i = 0
j = n-1
while i < n:
    sum1+=a[i][i]
    sum2+=a[i][j]
    i+=1
    j-=1
print(abs(sum1-sum2))
