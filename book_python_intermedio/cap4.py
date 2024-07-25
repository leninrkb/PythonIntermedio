#  map filter y reduce

# map
# aplicamos una funciond eentrada a cada elemetos del iterable que
# se pase como parametro

# elevar los numeros de unalista al cuadrado
# sin map

def println(arg):
    print(arg, end="\n\n")

mylist = [1,2,3,4,5]
newlist = []
for n in mylist:
    newlist.append(n**2)
println(newlist)

# con map
def pow2(n):
    return n**2

println(list(map(pow2, mylist)))

# con map y lambda
println(list(map(lambda n: n**2, mylist)))

# filter
# filtra los elemtos de una lista en base al criterio que se establezca

lista = range(20)
pares = list(filter(lambda n: n % 5 == 0, lista))
println(pares)

# reduce
# aplica operaciones sobre una lista y devuelve un unico resultado

# sin reduce
nums = range(1,5)
pro = 1
for n in nums:
    pro = pro * n
println(pro)

# con reduce
from functools import reduce
pro = reduce(lambda n, m: n * m, range(1,5))
println(pro)