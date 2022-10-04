import copy         # из этой библиотеки нам понадобится функция копирования объектов

# Создадим функцию для поиска координат (индексов) ближайшего пикселя к заданному в двумернои массиве
def get_nearest_x_y(x, y, array):           # передадим в качестве аргументов координаты пикселя и массив
    # Пройдём по всем строкам и столбцам массива и рассчитаем расстояние от каждого найденного пикселя до искомого
    length = round(((0-len(array))**2+(0-len(array[0]))**2)**0.5)+1                   # инициируем временную переменную длины значением, выходящим за пределы массива
    nearest_neighbour = -1                  # инициируем временную переменную яркости значением, выходящим за пределы яркости
    for each_x in range (len(array)):
        for each_y in range (len(array[each_x])):
            if each_x == x and each_y == y: continue                # если очередной пиксель имеет те же координаты, что и искомый - пропускаем шаг
            if array[each_x][each_y] != None and ((x-each_x)**2+(y-each_y)**2)**0.5 < length:
                length = ((x-each_x)**2+(y-each_y)**2)**0.5         # запоминаем текущее минимальное расстояние
                nearest_neighbour_x = each_x                         # запоминаем координату этого пикселя
                nearest_neighbour_y = each_y                         # запоминаем координату этого пикселя
            
            # if array[x] != None: return x           # проверяем что пиксель, координату которого нам передали, действительно не имеет значения яркости, а если имеет - то он сам себе ближайший сосед
            
            # if abs(x - each_x) < length and array[each_x] != None:  # если расстояние между очередным пикселем и искомым меньше хранящегося в временной переменной и этот пиксель не пустой
    return nearest_neighbour_x, nearest_neighbour_y              # после обхода всех пикселей возвращаем координаты пикселя с минимальным расстоянием

def fill_empty(array):                      # создаём функцию заполнения яркости пустых пикселей
    filled_pixels = copy.deepcopy(array)    # для упрощения кода будем заполнять копию исходного массива
    for each_x in range(len(filled_pixels)):
        for each_y in range (len(filled_pixels[each_x])):    # перебираем все элементы массива
            if filled_pixels[each_x][each_y] == None:       # как только находим пустой
                filled_pixels[each_x][each_y] = array[get_nearest_x_y(each_x, each_y, array)[0]][get_nearest_x_y(each_x, each_y, array)[1]]     # присваиваем ему значение ближайшего пикселя ИСХОДНОГО массива (чтобы не было ложных соседей)
    return filled_pixels                    # возвращаем заполненный массив


