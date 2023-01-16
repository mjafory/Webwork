p = 131
alpha = 2
kE = kM = None
y1 = 48
y2 = 84
x1 = 1

# Find kE/kM by dividing y1/alpha^kE mod p
for i in range(1, p):
    if (pow(alpha, i, p) == y1/alpha):
        kE = i
        break

# Calculate x2
x2 = (y2 * pow(y1, p-2, p)) % p

print("Masking key kM: ", kE)
print("Plaintext x2: ", x2)
