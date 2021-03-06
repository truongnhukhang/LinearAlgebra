from math import acos, cos, degrees

from vector.Line import Line
from vector.LinearSystem import LinearSystem
from vector.Plane import Plane
from vector.Vector import Vector


def vector_exercise():
    my_Vector = Vector([8.218, -9.341])
    my_Vector2 = Vector([-1.129, 2.111])
    print(my_Vector == my_Vector2)
    print(my_Vector + my_Vector2)
    my_Vector = Vector([7.119, 8.215])
    my_Vector2 = Vector([-8.223, 0.878])
    print(my_Vector - my_Vector2)
    my_Vector = Vector([1.671, -1.012, -0.318])
    print(my_Vector.scalar(7.41))
    my_Vector = Vector([-0.221, 7.437])
    print(my_Vector.magnitude())
    my_Vector = Vector([8.813, -1.331, -6.247])
    print(my_Vector.magnitude())
    my_Vector = Vector([5.581, -2.136])
    print(my_Vector.normalized())
    my_Vector = Vector([1.996, 3.108, -4.554])
    print(my_Vector.normalized())
    my_Vector = Vector([7.887, 4.138])
    my_Vector2 = Vector([-8.802, 6.776])
    print(my_Vector.dotProduct(my_Vector2))
    my_Vector = Vector([-5.955, -4.904, -1.874])
    my_Vector2 = Vector([-4.496, -8.755, 7.103])
    print(my_Vector.dotProduct(my_Vector2))
    my_Vector = Vector([3.183, -7.627])
    my_Vector2 = Vector([-2.668, 5.319])
    print(my_Vector.angle_between(my_Vector2))
    my_Vector = Vector([7.35, 0.221, 5.188])
    my_Vector2 = Vector([2.751, 8.259, 3.985])
    print(my_Vector.angle_between(my_Vector2, True))
    my_Vector = Vector([-7.579, -7.88])
    my_Vector2 = Vector([22.737, 23.64])
    print(my_Vector.isParallelWith(my_Vector2))
    print(my_Vector.isOrthogonalWith(my_Vector2))
    my_Vector = Vector([-2.328, -7.284, -1.214])
    my_Vector2 = Vector([-1.821, 1.072, -2.94])
    print(my_Vector.isParallelWith(my_Vector2))
    print(my_Vector.isOrthogonalWith(my_Vector2))
    my_Vector = Vector([3.039, 1.879])
    my_Vector2 = Vector([0.825, 2.036])
    print(my_Vector.findProjectorOn(my_Vector2))
    my_Vector = Vector([-9.88, -3.264, -8.159])
    my_Vector2 = Vector([-2.155, -9.353, -9.473])
    print(my_Vector.findOrthogonalOn(my_Vector2))
    my_Vector = Vector([3.009, -6.172, 3.692, -2.51])
    my_Vector2 = Vector([6.404, -9.144, 2.759, 8.718])
    print(my_Vector.findProjectorOn(my_Vector2))
    print(my_Vector.findOrthogonalOn(my_Vector2))
    my_Vector = Vector([8.462, 7.893, -8.187])
    my_Vector2 = Vector([6.984, -5.975, 4.778])
    print(my_Vector.crossProductWith(my_Vector2))
    my_Vector = Vector([-8.987, -9.838, 5.031])
    my_Vector2 = Vector([-4.268, -1.861, -8.866])
    print(my_Vector.crossProductWith(my_Vector2).magnitude())
    my_Vector = Vector([1.5, 9.547, 3.691])
    my_Vector2 = Vector([-6.007, 0.124, 5.772])
    print(my_Vector.crossProductWith(my_Vector2).magnitude() / 2)
def line_exercise() :
    # vector = Vector([4.046,2.836])
    # line = Line(vector,1.21)
    # vector2 = Vector([10.115,7.09])
    # line2 = Line(vector2,3.025)
    # print(line.isParalleWith(line2))
    # print(line.isEqualWith(line2))
    # print(line.intersectionWith(line2))
    # vector = Vector([7.204, 3.182])
    # line = Line(vector, 8.68)
    # vector2 = Vector([8.172, 4.114])
    # line2 = Line(vector2, 9.883)
    # print(line.isParalleWith(line2))
    # print(line.isEqualWith(line2))
    # print(line.intersectionWith(line2))
    vector = Vector([1.182, 5.562])
    line = Line(vector, 6.744)
    vector2 = Vector([1.773, 8.343])
    line2 = Line(vector2, 9.525)
    print(line.isParalleWith(line2))
    print(line.isEqualWith(line2))
    print(line.intersectionWith(line2))
def plane_exercise() :
    vector = Vector([-0.412, 3.806, 0.728])
    plane = Plane(vector,-3.46)
    vector2 = Vector([1.03, -9.515, -1.82])
    plane2 = Plane(vector2,8.65)
    print(plane.isParalleWith(plane2))
    print(plane.isEqualWith(plane2))

    vector = Vector([2.611, 5.528, 0.283])
    plane = Plane(vector, 4.6)
    vector2 = Vector([7.715, 8.306, 5.342])
    plane2 = Plane(vector2, 3.76)
    print(plane.isParalleWith(plane2))
    print(plane.isEqualWith(plane2))

    vector = Vector([-7.926, 8.625, -7.217])
    plane = Plane(vector, -7.952)
    vector2 = Vector([-2.642, 2.875, -2.404])
    plane2 = Plane(vector2, -2.443)
    print(plane.isParalleWith(plane2))
    print(plane.isEqualWith(plane2))

def linear_system_exercise() :
    p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
    p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
    p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
    p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')

    s = LinearSystem([p0, p1, p2, p3])
    s.swap_rows(0, 1)
    if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
        print('test case 1 failed')

    s.swap_rows(1, 3)
    if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
        print
        'test case 2 failed'

    s.swap_rows(3, 1)
    if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
        print
        'test case 3 failed'

    s.multiply_coefficient_and_row(1, 0)
    if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
        print
        'test case 4 failed'

    s.multiply_coefficient_and_row(-1, 2)
    if not (s[0] == p1 and
            s[1] == p0 and
            s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
            s[3] == p3):
        print
        'test case 5 failed'

    s.multiply_coefficient_and_row(10, 1)
    if not (s[0] == p1 and
            s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
            s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
            s[3] == p3):
        print
        'test case 6 failed'

    s.add_multiple_times_row_to_row(0, 0, 1)
    if not (s[0] == p1 and
            s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
            s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
            s[3] == p3):
        print
        'test case 7 failed'

    s.add_multiple_times_row_to_row(1, 0, 1)
    if not (s[0] == p1 and
            s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
            s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
            s[3] == p3):
        print
        'test case 8 failed'

    s.add_multiple_times_row_to_row(-1, 1, 0)
    if not (s[0] == Plane(normal_vector=Vector(['-10', '-10', '-10']), constant_term='-10') and
            s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
            s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
            s[3] == p3):
        print
        'test case 9 failed'

if __name__ == '__main__':
    p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
    p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
    p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
    p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
    s = LinearSystem([p0, p1, p2, p3])
    print(s.indices_of_first_nonzero_terms_in_each_row())