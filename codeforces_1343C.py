t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    i = 0

    while i < n:
        best = a[i]

        while i < n and (a[i] > 0) == (best > 0):
            best = max(best, a[i])
            i += 1

        ans += best

    print(ans)
