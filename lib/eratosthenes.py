# -*- coding: utf-8 -*-


""" Решето Эратосфена: просеиваем через него заданный список чисел и получаем все простые числа в нём """
def eratosthenes(x):
    analyzed_numbers = list(range(int(x + 1)))
    analyzed_numbers[1] = 0
    for i in analyzed_numbers:
        if i == 0:
            continue
        for j in range(i * 2, len(analyzed_numbers), i):
            analyzed_numbers[j] = 0
    primes = list(filter(None, analyzed_numbers))

    return primes
