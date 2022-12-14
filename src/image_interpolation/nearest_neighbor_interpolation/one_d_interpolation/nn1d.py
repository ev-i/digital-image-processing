import copy         # из этой библиотеки нам понадобится функция копирования объектов
# Создадим функцию для поиска координат (индекса) ближайшего пикселя к заданному в одномерном массиве
def get_nearest_x(x, array):                # передадим в качестве аргументов координату пикселя (индекс в массиве) и массив
    if array[x] != None: return x           # проверяем что пиксель, координату которого нам передали, действительно не имеет значения яркости, а если имеет - то он сам себе ближайший сосед
    length = len(array)+1                   # инициируем временную переменную длины значением, выходящим за пределы массива
    nearest_neighbour = -1                  # инициируем временную переменную яркости значением, выходящим за пределы яркости
    for each_x in range(len(array)):        # перебираем все пиксели
        if each_x == x: continue            # если очередной пиксель имеет те же координаты, что и искомый - пропускам шаг
        if abs(x - each_x) < length and array[each_x] != None:  # если расстояние между очередным пикселем и искомым меньше хранящегося в временной переменной и этот пиксель не пустой
            nearest_neighbour = each_x      # запоминаем координату этого пикселя
            length = abs(x - each_x)        # запоминаем текущее минимальное расстояние
    return nearest_neighbour                # после обхода всех пикселей возвращаем координаты пикселя с минимальным расстоянием

# создаём функцию заполнения яркости пустых пикселей
def fill_empty(array):                      
    filled_pixels = copy.deepcopy(array)    # для упрощения кода будем заполнять копию исходного массива
    for each_x in range(len(filled_pixels)):    # перебираем все элементы массива
        if filled_pixels[each_x] == None:       # как только находим пустой
            filled_pixels[each_x] = array[get_nearest_x(each_x, array)]     # присваиваем ему значение ближайшего пикселя ИСХОДНОГО массива (чтобы не было ложных соседей)
    return filled_pixels                    # возвращаем заполненный массив

