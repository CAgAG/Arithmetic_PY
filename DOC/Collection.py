# update(增加元素)

import collections
obj = collections.Counter(['11','22'])
obj.update(['22','55'])
#输出：Counter({'22': 2, '11': 1, '55': 1})

# subtract(原来的元素减去新传入的元素)

obj = collections.Counter(['11','22','33'])
obj.subtract(['22','55'])
#输出：Counter({'11': 1, '33': 1, '22': 0, '55': -1})