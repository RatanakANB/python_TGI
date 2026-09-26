def f(x):
    fx = (x*x) - (0.5*x) +5
    if fx > 0:
        return  f'x = {fx} is not a zero of the function'
    else:
        return f'x = {fx} is a zero of the function'

print(f(1))