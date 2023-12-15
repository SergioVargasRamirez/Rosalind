#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

generations = 33

#litter_size represents the number of new pairs produced by a rabbit
litter_size = 3


def Fibonacci(n, k):
    if n < 3:
        return 1
    else:
        # Fibonacci(n-1) represents the number of adult rabbits
        # Fibonacci(n-2) represents the number of young rabbits
        return Fibonacci(n-1, k) + Fibonacci(n-2,k)*k


print(Fibonacci(generations, litter_size))
