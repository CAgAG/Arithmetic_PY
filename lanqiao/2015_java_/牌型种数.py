def flag(num):
    if num > 13: return True
    return False

if __name__ == '__main__':
    count = 0
    result = [0]*13
    for a1 in range(5):
        result[0] = a1
        for a2 in range(5):
            result[1] = result[0] + a2
            for a3 in range(5):
                result[2] = result[1] + a3
                for a4 in range(5):
                    result[3] = result[2] + a4
                    if flag(result[3]):
                        break
                    for a5 in range(5):
                        result[4] = result[3] + a5
                        if flag(result[4]):
                            break
                        for a6 in range(5):
                            result[5] = result[4] + a6
                            if flag(result[5]):
                                break
                            for a7 in range(5):
                                result[6] = result[5] + a7
                                if flag(result[6]):
                                    break
                                for a8 in range(5):
                                    result[7] = result[6] + a8
                                    if flag(result[7]):
                                        break
                                    for a9 in range(5):
                                        result[8] = result[7] + a9
                                        if flag(result[8]):
                                            break
                                        for a10 in range(5):
                                            result[9] = result[8] + a10
                                            if flag(result[9]):
                                                break
                                            for a11 in range(5):
                                                result[10] = result[9] + a11
                                                if flag(result[10]):
                                                    break
                                                for a12 in range(5):
                                                    result[11] = result[10] + a12
                                                    if flag(result[11]):
                                                        break
                                                    for a13 in range(5):
                                                        result[12] = result[11] + a13
                                                        if flag(result[12]):
                                                            break
                                                        if result[12] == 13:
                                                            count += 1
                                                            print(count)
    print(count)

