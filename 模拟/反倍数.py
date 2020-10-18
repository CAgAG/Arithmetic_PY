num = int(input())
abc = input().strip().split(' ')
abc = [int(i) for i in abc]

n = 0
for i in range(num):
    if (i%abc[0]!=0) and (i%abc[1]!=0) and (i%abc[2]!=0):
        n += 1
print(n)

