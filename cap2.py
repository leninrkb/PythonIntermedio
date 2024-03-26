# depurando
# para depurar un archivo: python -m pdb my_script.py

import pdb

n = 10
a = 0
b = 1
c = 1
i = 0
while(i < n):
    print(a)
    pdb.set_trace()
    a = b
    b = c
    c = a + b
    i += 1