def central_tendency(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    mode = max(set(numbers), key=numbers.count)
    numbers.sort()
    if n % 2 == 0:
        median = (numbers[n//2-1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    print("Среднее значение: ", mean)
    print("Мода: ", mode)
    print("Медиана: ", median)

    if mean == median == mode:
        print("Распределение является симметричным")
    elif mean > median > mode or mean < median < mode:
        print("Распределение является асимметричным")
    else:
        print("Распределение является нормальным")

import random
numbers = [random.randint(0, 100) for _ in range(100)]   

