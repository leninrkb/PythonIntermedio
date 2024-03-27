# estructura de datos SET
# es como una lista, pero inmutable
# no puede contener elementos duplicados

ns = [9,7,6,5,1,2,3,4,"s","a","z","b"]
myset = set([n for n in ns])
print(myset)

# interseccion
set1 = set([1,4,5,6,7,6,5,7,6,8,7,9,8,0,3])
set2 = set([5,8,7,6,1,3,2,4,5,3,45])
print(set1.intersection(set2))

# diferencia
# no es lo mismo A - B, que B - A
set1 = set(["lenin","sana","hayase","hiyori"])
set2 = set(["sana","tohka","hayase","roxy"])

print(set1.difference(set2))
print(set2.difference(set1))

# tambien puedo crear sets con {}

set1 = {"hayase","hiyori","tohka","hayase"}
print(type(set1))
print(set1)