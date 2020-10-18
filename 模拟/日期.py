from datetime import datetime

if __name__ == '__main__':
    ymd, hms = input().strip().split(' ')
    ymd2, hms2 = input().strip().split(' ')

    ymd2 = ymd2.split('-')
    hms2 = hms2.split(':')
    ymd = ymd.split('-')
    hms = hms.split(':')

    nowTime = datetime(int(ymd[0]), int(ymd[1]), int(ymd[2]),
                                int(hms[0]), int(hms[1]), int(hms[2]))

    overTime = datetime(int(ymd2[0]), int(ymd2[1]), int(ymd2[2]),
                                 int(hms2[0]), int(hms2[1]), int(hms2[2]))

    c = overTime - nowTime

    tp = c.days * 24 * 3600
    tp += c.seconds

    tp *= 1000
    print(tp)
