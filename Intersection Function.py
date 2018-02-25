def intersection (a,b):
    c=[value for value in a if value in b]
    return c
def intersect(a,b):
    return list(set(a) and set(b))
a = [1,4,5,7,8,12]
b = [4,5,9,12,15,2]
c = (intersect(a,b))
print(intersection(a,b))

