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
