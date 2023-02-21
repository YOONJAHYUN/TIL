from itertools import permutations
from pprint import pprint

a = range(1, 4)
b = list(permutations(a, 2))
for i in b:
    print(i)