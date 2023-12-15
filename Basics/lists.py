#!/usr/bin/env python3

"""

Sergio Vargas, 2023
sergio.vargas@lmu.de

CC-BY 4.0

"""

random_phrase = 'Lphvg1MGNeophronJNqBF2rg2dTH1T7cD9ILW' \
                '7sseA1H9weZzQsw32rhA1xah3Nxi80zXIP9UU' \
                '3mugodjaricusaVnHTZhfQJDJmJ7wilv9LaXC' \
                'vxsJAXdPadHdzFmXvQMuGCwl6q0EdOmS75WSn' \
                'yBySFGW30j7iZ3mVyq4R.'

first_index = 8
second_index = 15
third_index = 75
fourth_index = 86

new_phrase = random_phrase[first_index:second_index+1] \
             + ' ' \
             + random_phrase[third_index:fourth_index+1]

print(random_phrase)
print(new_phrase)


