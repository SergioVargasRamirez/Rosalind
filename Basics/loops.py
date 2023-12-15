#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

first_index = 4754
second_index = 9525

sum_of_odds = 0

for i in range(first_index, second_index+1):
    if i % 2 != 0:
        sum_of_odds = sum_of_odds + i

print(sum_of_odds)
