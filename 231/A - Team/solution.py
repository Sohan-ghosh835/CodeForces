count = 0 #??
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        count += 1
print(count)