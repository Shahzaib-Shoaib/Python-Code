
# Defining Function

def f(x):
    return (x**3)+(x**2)-3*x-3


# Implementing Bisection Method


def bisection(a, b, e):
    step = 1
    condition = True
    while condition:
        mid = (a + b)/2
        print('Iteration-%d, mid = %0.6f and f(mid) = %0.6f' %
              (step, mid, f(mid)))
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        step = step + 1
        condition = abs(f(mid)) > e
    print('\nRequired Root is : %0.8f' % mid)


a = float(input('First Guess: '))
b = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and bisecting
if f(a) * f(b) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(a, b, e)
