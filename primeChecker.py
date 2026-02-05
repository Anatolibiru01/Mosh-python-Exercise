def prime_check(x):
    if x % 2 != 0 or x == 2:
        if x < 9 and (x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0):
            return f"{x} is a prime number"
        elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
            return f"{x} is not prime number"
        else:
            return f"{x} is a prime number"
    else:
        return f"{x} is not prime number"


print(prime_check(9))