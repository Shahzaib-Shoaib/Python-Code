def f(x):
    return x**3 + 2*x**2 + 4*x + 7

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

# Define the point at which to compute the derivative
x = 3

# Define the step size (h)
h = 0.0001

# Calculate the derivative using the forward difference formula
derivative = forward_difference(f, x, h)

# Print the derivative
print(derivative)
