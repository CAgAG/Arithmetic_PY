# https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/submissions/

if __name__ == '__main__':
    s = "We are happy."

    res = ''
    for i in s:
        if i != ' ':
            res += i
        else:
            res += '%20'
    print(res)
    print(s.replace(' ', '%20'))
    print('%20'.join(s.split(' ')))