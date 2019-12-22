from statistics import median

input()

X = [int(x) for x in input().split(" ")]
F = [int(x) for x in input().split(" ")]

arr = []

for idx,value in enumerate(X):
    arr = arr + [value] * F[idx]

arr = sorted(arr)

n = len(arr)

odd_len = n % 2

if(n%2 == 0):
    mid = int(n / 2)
else:
    mid = n // 2 + 1

L = arr[:mid]
U = arr[mid:]

Q1 = round(median(L),1)
Q3 = round(median(U),1)

print(round(float(Q3-Q1), 1))
