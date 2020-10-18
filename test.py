import itertools

for comb in itertools.product('1234', repeat=3):
    print(comb)