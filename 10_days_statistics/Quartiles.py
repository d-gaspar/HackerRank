from statistics import median

n = int(input())

arr = [int(x) for x in input().split(" ")]
arr = sorted(arr)

odd_len = n % 2

if(n%2 == 0):
    mid = int(n / 2)
else:
    mid = n // 2 

L = arr[:mid]
U = arr[(mid + odd_len):]

Q1 = int(median(L))
Q2 = int(median(arr))
Q3 = int(median(U))

print(Q1)
print(Q2)
print(Q3)
