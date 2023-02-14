# 1. Python program to convert the temperature in degree centigrade to Fahrenheit
import math


def centigradeToFahrenheit(celcius):
    return (celcius*1.8) + 32

# 2. Python program to find the area of a triangle whose sides are given
def areaTriangle(length,width):
    return 0.5*length*width

# 3. Python program to find out the average of a set of integers
def avarage(setOfNumbers):
    return sum(setOfNumbers)/len(setOfNumbers)

# 4. Python program to find the product of a set of real numbers
def product(setOfNumbers):
    if len(setOfNumbers) == 0:
        return -1
    product = 1
    for i in setOfNumbers:
        product *= i
    return product

# 5. Python program to find the circumference and area of a circle with a given radius
def cicumferenceAndArea(radius):
    # [circumference , area]
    return [2*math.pi*radius,math.pi*radius*radius]

# 6. Python program to check whether the given integer is a multiple of both 5 and 7

def checkIfMulOf5and7(number):
    if number%5==0 and number%7==0:
        return True
    if number%5==0:
        return True
    if number%7==0:
        return True
    return False

# 7. Python program to find the average of 10 numbers using while loop

def avgOf10():
    sum=0
    totalNumbers = 10
    i=1
    while i<11:
        sum+=i
        i+=1
    return sum/totalNumbers

# 8. Python program to display the given integer in a reverse manner

def intReverse(number):
    return int(str(number)[::-1])


# 9.Python program to find the geometric mean of n numbers
def geoMetricMean(numberList):
    # formula = mul(numberlist)**(1/n)
    multi = product(numberList)
    return multi**(1/len(numberList))

# 10.Python program to find the roots of a quadratic equation

def rootsOfQuadEq(a,b,c):
    # [root 1,root 2]
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))

    if d > 0:
        return [(-b + sqrt_val) / (2 * a),(-b - sqrt_val) / (2 * a)]
    elif d == 0:
        return [(-b / (2 * a))]



print("faherenheit : ",centigradeToFahrenheit(32))
print("Area of triangle : ",areaTriangle(4,5))
print("Avg of number : ",avarage([1,2,3,4]))
print("Product of set of list : ",product([2,3,4,5]))
print("Circum and area : ",cicumferenceAndArea(10))
print("Num is mul of 5 or 7 or both : ",checkIfMulOf5and7(35))
print("Avg of 10 : ",avgOf10())
print("Reversed : ",intReverse(1234))
print("Geometric mean : ",geoMetricMean([3,4,5,6]))
print("List of roots : ",rootsOfQuadEq(8,16,8))