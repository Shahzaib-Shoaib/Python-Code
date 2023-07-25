# Define the function f(x) and its derivative f'(x)
def f(x):
    return x**3 - 5*x**2 + 2

def f_prime(x):
    return 3*x**2 - 10*x

# Newton-Raphson method implementation
def newton_raphson(f, f_prime, x0, max_iterations, tolerance):
    for i in range(max_iterations):
        fx0 = f(x0)
        if abs(fx0) < tolerance:
            return x0
        f_prime_x0 = f_prime(x0)
        if f_prime_x0 == 0:
            break
        x1 = x0 - fx0 / f_prime_x0
        x0 = x1
    return x0

# Initial guess and maximum iterations for the method
initial_guess = 1.5
max_iterations = 1000
tolerance = 1e-10

# Find the root using the Newton-Raphson method
root = newton_raphson(f, f_prime, initial_guess, max_iterations, tolerance)

print("Approximate root:", root)
print("f(root) =", f(root))
