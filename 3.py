from math import sqrt

n = 600851475143

max_prime_factor = 0

while not n%2:
    n = n/2

for i in range(3, int(sqrt(n))+1, 2):
    while not n%i:
        n = n/i

        max_prime_factor = i

print(max_prime_factor)