# mundane Math adds all the even numbers between 1 and 100
import numpy

evennumbers = numpy.arange(2, 102, 2)

answer = sum(evennumbers)

print("The sum of even number between 1 and 100 is {0}".format(str(answer)))