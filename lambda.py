x = lambda i: i + 15
print(x(5))
print(x(7))

#putting arguments

y = lambda i, y, z: i + y + z

print(y(9, 4, 5))
print(y(40,30,20))

def new(b):
    return lambda d: d * b

double = new(5)
tripple = new(8)

print(double(4))
print(tripple(4))