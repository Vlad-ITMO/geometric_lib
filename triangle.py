def area(a, h):
    
    ''' возвращает площадь треугольника

                Параметры:
                      a(int): основание треугольника (одна из его сторон)
                      h(int): высота треугольника, опущенная на сторону а

                Возвращаемое значение:
                      произведение стороны а и высоты h, поделённое на 2 (т.е. площадь)
    '''

    if a <= 0 or h <= 0:
        raise ValueError("Длина стороны и высоты должны быть больше нуля!")

    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("a и h должны быть значением int или float")
    
    return a * h / 2

def perimeter(a, b, c):
    
    ''' возвращает периметер треуголльника

                Параметры:
                      a(int): первая сторона треугольника
                      b(int): вторая сторона треугольника
                      c(int): третья сторона треугольника

                Возвращаемое значение:
                      сумма всех трёх сторон треугольника (т.е. периметер)
    '''

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("стороны треугольника долны быть больше нуля")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("стороны треугольника должны быть значением int или float")

    if (a + b > c) and (a + c > b) and (b + c > a):
        return a + b + c
    else:
        raise ValueError("треугольника с такими сторонами не существует")
