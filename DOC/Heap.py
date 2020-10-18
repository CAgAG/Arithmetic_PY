"""
    堆, 优先队列
"""
import heapq

from Array import RandArr


# 快速实现堆排序, 类似于 nsmallest
def heapsort(Iter):
    h = []
    for i in Iter:
        heapq.heappush(h, i)
    return [heapq.heappop(h) for _ in range(len(h))]


# 快速实现堆排序, 类似于 nsmallest
def heapsortArr(arr: list):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


if __name__ == '__main__':
    arr = RandArr(10)

    MaxSort = heapq.nlargest(len(arr), arr)  # 类似于降序sort, 有key, 第一个为最大值
    MinSort = heapq.nsmallest(len(arr), arr)  # 类似于升序sort, 有key, 第一个为最小值
    print(MaxSort, MinSort)

    """
    heapify：对序列进行堆排序， 小根堆
    _heapify_max: 大根堆
    heappush:在堆序列中添加值
    heappop:删除最小值并返回, 即heap[0]
    _heappop_max: 删除最大值并返回
    heappushpop:添加并删除堆中最小值且返回，添加之后删除
    heapreplace:添加并删除队中最小值且返回，删除之后添加 --> 推荐使用
    _heapreplace_max: 添加并删除队中最大值且返回，删除之后添加 --> 推荐使用
    """
    heapq.heapify(arr)  # 进行一趟堆排序, 注 heap[0] 永远是最小的
    print(arr)
    print(heapq.heappop(arr))
    heapq.heappush(arr, -100)
    print(heapq.heappop(arr))

    # heapq._heapify_max(arr)  # 进行一趟堆排序, 注 heap[0] 永远是最大的
    # print(arr)
    # print(heapq._heappop_max(arr))
    # heapq.heappush(arr, 1000)
    # heapq._heapify_max(arr) # push后必须再建一次
    # print(heapq._heappop_max(arr))

    """
    merge：将多个已排序的输入合并为一个已排序的输出,
           假定每个输入流都是已排序的（从小到大）,
           返回一个可迭代对象
    """
    arr2 = [i for i in range(10)]
    arr3 = [i for i in range(12, 20)]
    print(list(heapq.merge(arr2, arr3)))

"""
    全部排序使用sorted,
    需要查找最大或最小的几个或者多个我们使用alargest/asmallest,
    查找最大最小使用max/min
"""
