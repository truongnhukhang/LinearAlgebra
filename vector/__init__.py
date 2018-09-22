from vector.Vector import Vector

if __name__ == '__main__':
    my_Vector = Vector([8.218,-9.341])
    my_Vector2 = Vector([-1.129,2.111])
    print(my_Vector==my_Vector2)
    print(my_Vector+my_Vector2)
    my_Vector = Vector([7.119,8.215])
    my_Vector2 = Vector([-8.223,0.878])
    print(my_Vector-my_Vector2)
    my_Vector = Vector([1.671,-1.012,-0.318])
    print(my_Vector.scalar(7.41))
