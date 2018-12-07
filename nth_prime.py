import math
def nth_prime_number(n):
    # initial prime number list
    prime_list = [2]
    # first number to test if prime
    num = 3
    # keep generating primes until we get to the nth one
    while len(prime_list) < n:
        flag = True
        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                flag = False
                # break to stop testing more numbers, we know it's not a prime
                break
            # check for prime condition square root
            if math.sqrt(num) < p:
                break

        # if it is a prime, then add it to the list
        # after a for loop, else runs if the "break" command has not been given
        if flag:
            # append to prime list
            prime_list.append(num)

        # don't check even numbers
        num += 2

    # return the last prime number generated
    return prime_list[-1]


if __name__ == "__main__":
     
     n = int(raw_input('Enter a number: '))
     print nth_prime_number(n)
