A = [543, 5346, 453, 3254, 1, 65, 7, 6455, 345, 3]
K = 0

LOC = K

MIN = A[K]

for J in range(len(A)):
    if MIN > A[J]:
        MIN = A[J]
        LOC = J

print(MIN, LOC)
