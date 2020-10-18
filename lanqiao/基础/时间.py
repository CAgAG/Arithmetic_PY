if __name__ == '__main__':
    Map = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
        12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty'
    }

    h, m = input().strip().split(' ')
    h = int(h)
    m = int(m)

    if m == 0:
        if h > 20:
            print(Map[20], Map[h-20], "o'clock")
        else:
            print(Map[h], "o'clock")
    else:
        if h > 20:
            if m > 20:
                if m % 10 == 0:
                    print(Map[20], Map[h-20], Map[m])
                else:
                    print(Map[20], Map[h - 20], Map[m // 10 * 10], Map[m % 10])
            else:
                print(Map[20], Map[h-20], Map[m])
        else:
            if m > 20:
                if m % 10 == 0:
                    print(Map[h], Map[m])
                else:
                    print(Map[h], Map[m // 10 * 10], Map[m % 10])
            else:
                print(Map[h], Map[m])


