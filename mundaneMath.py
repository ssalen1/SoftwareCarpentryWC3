"""
This file adds all the even numbers between 1 and 100
for weekly challenge 3
"""
import numpy

even_numbers = numpy.arange(2, 102, 2)

sum_even_numbers = sum(even_numbers)

print("The sum of even number between 1 and 100 is {0}".format(str(sum_even_numbers)))
