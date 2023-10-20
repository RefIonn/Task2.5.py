import random
while True:
    min = int(input('Введите минимальное значение в массиве: '))
    max = int(input('Введите максимальное значение в массиве: '))
    if min > max:
        print('Такого массива не существует')
    else:
        size = int(input('Введите размер массива: '))


        def fill_array(array, size):
            for i in range(size):
                array[i] = random.randint(min, max)


        array = [0] * size

        fill_array(array, size)
        print(array)
    print('Хотите ещё раз сгенерировать массив? ')
    repeat = input('Да или нет: ')
    if repeat in ['Да', 'да', 'lf', 'da']:
        continue
    else:
        break
