input()
# 在蓝桥杯这样做时, 注意会
# 多一个空字符
List = input().strip().split(' ')
List.sort(key=lambda x: int(x))
print(' '.join(List))



