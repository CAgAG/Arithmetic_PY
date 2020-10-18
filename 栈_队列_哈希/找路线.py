def Road(inputs: dict):
    # Reverse 和 inputs 键, 值相反
    Reverse = dict()
    for k, v in inputs.items():
        Reverse[v] = k

    start = None
    # 找到起始点
    for k, v in inputs.items():
        if k not in Reverse:
            start = k
            break
    if start is None:
        return None

    to = inputs[start]

    road = ''
    road += f'{start}->{to}'

    start = to
    to = inputs[to]
    while to is not None:
        road += f', {start}->{to}'
        start = to
        to = inputs.get(to, None)
    return road


if __name__ == '__main__':
    inputs = dict()
    inputs['a'] = 'b'
    inputs['c'] = 'd'
    inputs['b'] = 'c'
    inputs['d'] = 'e'

    print(Road(inputs))






