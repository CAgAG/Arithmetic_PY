import string

lower = list('abcdefghijklmnopqrstuvwxyz')
n_lower = lower[3:]+lower[:3]

S = list(input().strip())
for i in range(len(S)):
    index = lower.index(S[i])
    S[i] = n_lower[index]

print(''.join(S))


