n = int(input())
i = 0
res = ''
while len(res) < n:
    i += 1
    res += f'{i}' * i
res = res[:n]
print(res)