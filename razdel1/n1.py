from functools import partial

def if_even(func, x):
    if x % 2 == 0:
        return func(x)
    return x

if_even_inc = partial(if_even, lambda x: x + 1)
if_even_double = partial(if_even, lambda x: x * 2)
if_even_square = partial(if_even, lambda x: x ** 2)

print(if_even_inc(4))  
print(if_even_double(4))  
print(if_even_square(4))  
print(if_even_inc(3))  