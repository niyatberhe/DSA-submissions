n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

j = 0
answer = []

for x in b:
    while j < n and a[j] < x:
        j += 1

    answer.append(j)

print(*answer)
