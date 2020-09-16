import math

a = int(input("Input A: "))
b = int(input("Input B: "))
c = int(input("Input C: "))

def equator(a, b, c):
    global num_plus
    num_plus = (0-b + math.sqrt(b**2 - 4 * a * c) / 2)
    global num_minus
    num_minus = (0-b - math.sqrt(b**2 - 4 * a * c) / 2)
equator(a, b, c)
try: 
    print(f"X = {num_plus} or {num_minus}")
except Exception as e:
    print(e)
    print("The square root of", (b**2 - 4 * a * c))
