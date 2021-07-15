import random
import math


def f(x):
    """
    f is the function which we wish to integrate.

    :param x: the independent value
    :return: the output value of f(x)
    """
    return x**2


def calculate_integral(xmin, xmax, samples):
    """
    calculate_integral is the function responsible for actually approximating the integral of f(x)

    :param xmin: The minimum x-value
    :param xmax: The maximum x-value
    :param samples: The amount of random samples to take.

    :return: An estimate of the definite integral in [xmin; xmax]
    """
    # Step 1. Generate random x-values
    xrand = []
    
    for _ in range(samples):
        xrand.append(random.uniform(xmin, xmax))
    
    # Step 2. Calculate the average of all the values.
    average = 0

    for x in xrand:
        average += f(x)
    average /= samples

    # Step 3. Return the average multiplied by the range
    return average * (xmax - xmin)


def main():
    
    while True:
        runs = int(input("[*] Please enter the amount of times to approximate the integral (averaging): "))
        samples = int(input("[*] Amount of random samples: "))
        min = int(input("[*] Minimum x-value: "))
        max = int(input("[*] Maximum x-value: "))
        
        approximation = 0
        
        for _ in range(runs):
            approximation += calculate_integral(min, max, samples)
        approximation /= runs
        
        print("[+] Approximate definite integral value: {}".format(approximation))
    
    
if __name__ == "__main__":
    main()
