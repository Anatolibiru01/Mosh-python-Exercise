primes = []
for prime in range(2, 100):
    divisablity = prime % 2 == 0 or prime % 3 == 0 or prime % 5 == 0 or prime % 7 == 0
    if prime % 2 != 0 or prime == 2:
        if prime < 10 and divisablity:
            primes.append(prime)
        elif divisablity:
            pass
        else:
            primes.append(prime)

print(primes) 