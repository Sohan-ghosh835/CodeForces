t = int(input())
for _ in range(t):
    word = input()
    if len(word)<=10:
        print(word)
    else:
        l = word[0]
        r = word[-1]
        s = str(len(word) - 2)
        print(l+s+r)