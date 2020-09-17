import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def quad(a, b, c):
    try:
        return (0-b+math.sqrt(b**2-4*a*c))/(2*a), (0-b-math.sqrt(b**2-4*a*c))/(2*a)
    except Exception as e:
        return e

print("+ first, then - second:")
print(quad(a, b, c))
