input()
L = input().split(' ')
# 在蓝桥杯这样做时, 注意会
# 多一个空字符
L = [int(i) for i in L[:-1]]
print(max(L))
print(min(L))
print(sum(L))


