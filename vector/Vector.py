from decimal import Decimal
from math import sqrt, cos, pi, acos


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    def __add__(self, other):
        temp = []
        for index in range(self.dimension) :
            temp.append(self.coordinates[index] + other.coordinates[index])
        plus_vector = Vector(temp)
        return plus_vector
    def __sub__(self, other):
        temp = []
        for index in range(self.dimension):
            temp.append(self.coordinates[index] - other.coordinates[index])
        result = Vector(temp)
        return result
    def scalar(self,other):
        temp = []
        for index in range(self.dimension):
            temp.append(self.coordinates[index]*other)
        result = Vector(temp)
        return result
    def magnitude(self):
        total = 0
        for index in range(self.dimension):
            total = total + pow(self.coordinates[index],2)
        return sqrt(total)
    def normalized(self):
        magNumber = self.magnitude()
        try:
            unit = 1/magNumber
            return self.scalar(unit)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dotProduct(self,other):
        total = sum([x*y for x,y in zip(self.coordinates,other.coordinates)])
        return total
    def angle_between(self,other,in_degress = False):
        v1 = self.normalized()
        v2 = other.normalized()
        angle_in_radian = acos(round(v1.dotProduct(v2),3))
        if(in_degress):
            degress_per_radian = 180. / pi
            return degress_per_radian*angle_in_radian
        else:
            return angle_in_radian
    def isParallelWith(self,other):
        return self.is_zero() or other.is_zero() or self.angle_between(other)==0 or self.angle_between(other) == pi
    def isOrthogonalWith(self,other,tolerance=1e-10):
        return abs(self.dotProduct(other)) < tolerance
    def is_zero(self,tolerance=1e-10):
        return self.magnitude() < tolerance