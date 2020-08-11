'''
***MEAN, MEDIAN, MODE***

What can we learn from looking at a group of numbers?

In Machine Learning (and in mathematics) there are often three values that interests us:

    Mean - The average value
    Median - The mid point value
    Mode - The most common value

Example: We have registered the speed of 13 cars:

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

What is the average, the middle, or the most common speed value?

*MEAN*

The mean value is the average value.

To calculate the mean, find the sum of all values, and divide the sum by the number of values:

(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77

The NumPy module has a method for this.
'''

#Example
#Use the NumPy mean() method to find the average speed:
import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.mean(speed)

print(x)

print("-" * 50)

'''
*MEDIAN*

The median value is the value in the middle, after you have sorted all the values:

77, 78, 85, 86, 86, 86, *87*, 87, 88, 94, 99, 103, 111

It is important that the numbers are sorted before you can find the median.
'''

#Example
#Use the NumPy median() method to find the middle value:
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

print("-" * 50)


'''
If there are two numbers in the middle, divide the sum of those numbers by two.

77, 78, 85, 86, 86, *86*, *87*, 87, 94, 98, 99, 103

(86 + 87) / 2 = 86.5
'''

#Example
#Using the NumPy module:
import numpy

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

print("-" * 50)

'''
*MODE*

The Mode value is the value that appears the most number of times:

99, *86*, 87, 88, 111, *86*, 103, 87, 94, 78, 77, 85, *86* = 86

The SciPy module has a method for this:
'''

#Example
#Use the SciPy mode() method to find the number that appears the most:
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)
#The mode() method returns a ModeResult object that contains the mode number (86), and count (how many times the mode number appeared (3)).
