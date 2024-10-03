import math



def area(r):
    
    ''' возвращает площадь круга

                Параметры:
                      a(int): радиус круга

                Возвращаемое значение:
                      произведение числа pi и квадрат радиуса (т.е. площадь)
    '''
    
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be an integer or float")
    
    if r <= 0:
        raise ValueError("Radius must be a non-negative number")
    
    return math.pi * r * r 
''' osdvk '''

def perimeter(r):
    
    ''' возвращает периметер круга

                Параметры:
                      a(int): радиус круга

                Возвращаемое значение:
                      произведение числа два, числа pi и радиуса (т.е. периметер)
    '''
    
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be an integer or float")
    
    if r <= 0:
        raise ValueError("Radius must be a non-negative number")
    
    return 2 * math.pi * r

