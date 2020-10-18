import heapq

if __name__ == '__main__':
    input()
    arr = input().strip().split(' ')
    arr = [int(i) for i in arr]

    result = 0
    heapq.heapify(arr)
    while len(arr) != 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        S = a + b
        result += S
        arr.append(S)
    print(result)