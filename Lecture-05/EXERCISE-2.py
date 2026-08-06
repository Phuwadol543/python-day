def generate_primes(n):
    primes = ""
    for i in range(1, n + 1):
        if i > 1:
            for j in range(2, int(i**0.5)+1):
                if i % j == 0 :
                    break
            else:
                S = str(i)
                primes += S
    return (f'"{primes}')

print(generate_primes(10))
        