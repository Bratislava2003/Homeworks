"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*nums):
    result = [num ** 2 for num in nums]
    return result


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
    

def filter_numbers(list_of_nums, Filter = ODD):
    if Filter == ODD:
        res_odd = list(filter(lambda i: i % 2 != 0, list_of_nums))
        return res_odd
    elif Filter == EVEN:
        res_even = list(filter(lambda i: i % 2 == 0, list_of_nums))
        return res_even
    elif Filter == PRIME:   
        res_prime = list(filter(is_prime, list_of_nums))
        return res_prime


