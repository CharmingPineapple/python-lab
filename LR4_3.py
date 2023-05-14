# Вариант 15

# Вариант 29
from math import asin, exp, cos, sqrt, log, tan, pi


def f1(x):
    return z + abs(y ** 2 - x ** 2) + y * (asin(exp(-z + 5)))
# при условии из варианта asin не определен, т.к. не попадает в диапазон от -1 до 1


def f2(x):
    return sqrt((x - cos(y + z)**2)/(5 + log(y + 5*x / abs(x*y - sqrt(7)))))


y = 10
z = 11
a = 9
b = 12
h = 0.1
N = int(round((b-a)/h, 0))
for i in range(N+1):
    if (exp(-z + 5) >= -1) and (exp(-z + 5) <= 1):
        x = a + i*h
        print(f1(x) + f2(x))

print("-----------------")

def t1(x):
    return 1/(2*(n-1)*(x**(n-1))) + a/(2*n*x**n)

def t2(x):
    return (1/(2*a)) * pow(tan(a*x), 2) + (1/a)*log(cos(a*x))

n = 4
a = -pi/4
b = 2*pi
h = 0.05*pi
N = int(round((b-a)/h, 0))

for i in range(N+1):
    if x != 0:
        x = a + i * h
        print(t1(x) + t2(x))