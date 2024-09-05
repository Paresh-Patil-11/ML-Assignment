
def checkFactors(n):
    factors = []
    divisor = 2
    while (n > 1):
        count = 0
        while (n % divisor == 0):
            n //= divisor
            count +=1
        if (count > 0):
            factors.append((divisor,count))
        divisor += 1

    return factors

def main():
    number = 60
    result = checkFactors(number)
    print(result)
    

if __name__ == "__main__":
    main()