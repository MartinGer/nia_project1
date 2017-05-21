import random


def calc_maximum(string):
    result = 0
    for char in string:
        result += int(char)
    return result


def create_random_string(n):
    return ''.join(random.choices('01', k=n))


# algorithms

def algorithm_rls(n, test_function):
    counter = 0
    x = create_random_string(n)

    while calc_maximum(x) is not n:
        counter += 1
        y = x
        index = random.randint(0, n - 1)
        list_y = list(y)
        list_y[index] = str(1 - int(list_y[index]))
        y = ''.join(list_y)
        if test_function(y) >= test_function(x):
            x = y
    return counter


def algorithm_11_ea(n, test_function):
    counter = 0
    x = create_random_string(n)

    while calc_maximum(x) is not n:
        counter += 1
        y = x
        list_y = list(y)
        for idx, val in enumerate(list_y):
            if random.choices((True, False), (1 / n, 1 - (1 / n)))[0]:
                list_y[idx] = str(1 - int(val))

        y = ''.join(list_y)
        if test_function(y) >= test_function(x):
            x = y
        print(x)
    return counter


def algorithm_1lambda_ea(n, test_function):
    pass


# test_functions

def one_max(string):
    result = 0
    for char in string:
        result += int(char)
    return result


def leading_ones(string):
    result = 0
    for char in string:
        if char == '0':
            return result
        result += int(char)
    return result


def jump_k(string):
    pass


def bin_val(string):
    return int(string, 2)


def royal_roads(string):
    pass


print(algorithm_11_ea(25, leading_ones))
