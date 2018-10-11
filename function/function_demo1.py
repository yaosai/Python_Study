import math

print('hello,world')


def my_function(x):
    if not isinstance(x, (int, float)):
        return TypeError('error type')
    if x > 0:
        return x
    else:
        return 0


def null_function():
    pass


print(my_function(100))
print(my_function(-50))
print(my_function('A'))


def quadratic(a, b, c):
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / 2 * a
        x2 = (-b - math.sqrt(d)) / 2 * a
        return x1, x2
    else:
        print('无解或只有一个解')


print(quadratic(2, 5, 3))


def power(x=3, n=4):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(n=2))
