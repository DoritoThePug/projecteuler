import math

def find_num_of_prime_factors(numbers):
    num_prime_factors = {}

    for num in numbers:
        t_num = num
        t_num_prime_factors = {}

        while t_num%2 == 0:
            # prime_factors[num] = prime_factors.get(num, []) + [2]
            t_num_prime_factors[2] = t_num_prime_factors.get(2, 0) + 1
            t_num = t_num//2

        for i in range(3, int(math.sqrt(num))+1, 2):
            if t_num%i == 0:
                # prime_factors[num] = prime_factors.get(num, []) + [i]
                t_num_prime_factors[i] = t_num_prime_factors.get(i, 0) + 1

                t_num = t_num//i

        if t_num >= 2:
            # prime_factors[num] = prime_factors.get(num, []) + [t_num]

            t_num_prime_factors[t_num] = t_num_prime_factors.get(t_num, 0) + 1

        for factor, num_of in t_num_prime_factors.items():
            if num_prime_factors.get(factor, 0) < num_of:
                num_prime_factors[factor] = num_of
        

        

    return num_prime_factors

result = 1

for num, num_of in find_num_of_prime_factors(list(range(1, 21))).items():
    result *= num ** num_of

print(result)