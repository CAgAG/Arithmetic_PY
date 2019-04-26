#小数及整数运算
import re
from functools import reduce

def check_right(data_input):
    if data_input.count('(') != data_input.count(')'):
        data_input = ''
        print('请输入正确算式')
    return data_input

def check_int(s):
    if '.' in s:
        return float(s)
    else:
        return int(s)

def strip_data(data):
    #处理数据字符串
    data = re.sub('[() ]', '', data)
    if '+-' in data:
        data = data.replace('+-', '-')
    if '-+' in data:
        data = data.replace('-+', '-')
    if '--' in data:
        data = data.replace('--', '+')
    if '++' in data:
        data = data.replace('++', '+')
    if '*+' in data:
        data = data.replace('*+', '*')
    if '/+' in data:
        data = data.replace('/+', '/')
    return data

def calculating(striped_data):
    #计算+-*/
    if '/' in striped_data:
        data = re.findall(r'[-]?[\deE\.]+/[-/\deE\.]+', striped_data)
        for ele in data:
            ele = re.sub(r'(?<=[-\deE\.])-[-]?[\deE\.]+', '', ele)
            try:
                result = round(reduce(lambda x, y:x/y, list(map(check_int, ele.split('/')))), 4)
                striped_data = strip_data(striped_data.replace(ele, str(result)))
            except ZeroDivisionError as e:
                print('0不能作为除数')
                striped_data = ''
                break

    if '*' in striped_data:
        data = re.findall(r'[-]?[\deE\.]+\*[-*\deE\.]+', striped_data)
        for ele in data:
            ele = re.sub(r'(?<=[-\deE\.])-[-]?[\deE\.]+', '', ele)
            result = round(reduce(lambda x, y:x*y, list(map(check_int, ele.split('*')))), 4)
            striped_data = strip_data(striped_data.replace(ele, str(result)))

    if '+' in striped_data:
        data = re.findall(r'[-]?[\deE\.]+[+\deE\.]+', striped_data)
        for ele in data:
            if not ele:
                #防止空错误
                continue
            if 'e+' in ele:
                ti = ele.split('e+')
                result = float(ti[0])*(10**int(ti[1]))
            else:
                result = round(reduce(lambda x, y:x+y, list(map(check_int, ele.split('+')))), 4)
            striped_data = strip_data(striped_data.replace(ele, '+'+str(result)))

    if '-' in striped_data:
        data = re.findall(r'[-]?[\deE\.]+[-\deE\.]+', striped_data)
        for ele in data:
            if ele.startswith('-'):
                #防止负数开头导致运算失败
                ele_temp = ele.lstrip('-')
                ele_new = ele_temp.split('-')
                ele_new[0] = '-'+ele_new[0]
            else:
                ele_new = ele.split('-')
            result = round(reduce(lambda x, y:x-y, list(map(check_int, ele_new))), 4)
            striped_data = strip_data(striped_data.replace(ele, str(result)))
    return striped_data

if __name__ == '__main__':

    deal = re.compile("\([^()]+\)")
    choice = True
    data_input = check_right(input('请输入计算式(quit 离开)>>>'))

    while choice:
        data = re.search(deal, data_input)
        if data:
            striped_data = strip_data(data.group())
            data_2 = calculating(striped_data)
            data_input = data_input.replace(data.group(), data_2)
        else:
            data_2 = calculating(strip_data(data_input))
            result = calculating(data_2)
            print('结果: ',result)
            data_input = check_right(input('请输入计算式(quit 离开)>>>'))
        if data_input == 'quit':
            choice = False
