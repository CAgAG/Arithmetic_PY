if __name__ == '__main__':
    arr1 = [
        i for i in range(10)
    ]

    arr2 = [
        i for i in range(5, 15)
    ]

    print(set(arr1) - set(arr2))

    print(arr1 * 2)
    print(arr1 + arr2)

    ta = [
        1, 2, 3,
    ]
    tb = [
        2, 1, 3
    ]
    print(ta == tb)