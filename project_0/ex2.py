'''Игра - "Угадай число"
компьютер сам загадывает и угадывает число максимум за 20 попыток
'''

import numpy as np

def random_predict(number: int=1) -> int:    
    """ Рандомно угадываем число

    Args:
        number (int, optional): _загаданное число_. Defaults to 1.

    Returns:
        int: _число попыток_
    """
    
    count = 0  # количество попыток
    limit_a = 1 # Минимально возможное загаданное число
    limit_b = 101 # Максимально возможное загаданное число + 1
        
    predict_number = np.random.randint(limit_a, limit_b) # Определяем предполагаемое число   
    
    while True:
        count += 1

        # Если предполагаемое число больше загаданного, то 
        if predict_number > number:     
            limit_b = predict_number - 1   # переопределяем  максимально возможное загаданное число 
            predict_number = ( limit_b + limit_a) // 2  # определяем предполагаемое число как среднее между максимально и минимально возможным  

        # Если предполагаемое число меньше загаданного, то 
        elif predict_number < number:
            limit_a = predict_number + 1   # переопределяем  минимально возможное загаданное число 
            predict_number = ( limit_b + limit_a) // 2  # определяем предполагаемое число как среднее между максимально и минимально возможным 

        else:
            break  # конец игры- выходим из цикла
    return count





def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

 #RUN
if __name__ == '__main__':
    score_game(random_predict)
    
