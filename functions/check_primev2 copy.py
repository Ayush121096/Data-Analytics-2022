def check_prime(n): # check prime no between given numbers
    for i in range(1,13):
        if n % i == 0:
            return('prime') #return is used play again and again
            break
    else:
            return('not prime')

for i in range(2,100):
    out = check_prime(i)
    print(i, out)
    