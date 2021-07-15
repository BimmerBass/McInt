import random


def f(x):
    """
    f is the function which we wish to integrate.

    :param x: the independent value
    :return: the output value of f(x)
    """
    return x**2


def random_num(start, end):
    """
    random_num computes a random number in the range [start;end]
    
    :param start: the starting value
    :param end: the ending value
    :return: a floating-point number between start and end
    """
    return random.randrange(start, end)



def calculate_integral(xmin, xmax, samples):
    """
    calculate_integral is the function responsible for actually approximating the integral of f(x)

    :param xmin: The minimum x-value
    :param xmax: The maximum x-value
    :param samples: The amount of random samples to take.

    :return: An estimate of the definite integral in [xmin; xmax]
    """
    # Step 1. Take random samples of the function values
    values = []

    for _ in range(samples):
        values.append(random_num(xmin, xmax))
    
    # Step 2. Calculate the average of all the values.
    average = 0

    for value in values:
        average += value
    average /= samples

    # Step 3. Return the average multiplied by the range
    return average * (xmax - xmin)