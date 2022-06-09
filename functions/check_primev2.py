def check_prime():
    a = 1
    for i in range(1,13):
        if a % i ==0:
            return('not prime') #return is used play again and again
            break
    else:
            return('prime')

out = check_prime()
print(out)
