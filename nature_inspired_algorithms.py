import random


def calc_maximum(string):
    result = 0
    for char in string:
        result += int(char)
    return result


def create_random_string(n):
    return ''.join(random.choices('01', k=n))

def split_string(n, st):
    lst = [""]
    for i in str(st):
        l = len(lst) - 1
        if len(lst[l]) < n: 
            lst[l] += i
        else:
            lst += [i]
    return lst

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
        #-------------------------------------------------------------- print(x)
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
        #-------------------------------------------------------------- print(x)
    return counter


def algorithm_1lambda_ea(n, test_function):
    counter = 0
    x = create_random_string(n)

    while calc_maximum(x) is not n:
        counter += 1
        y = x
        list_y = list(y)
        lamb = random.randint(0, n - 1)
        for idx, val in enumerate(list_y):
            if idx <= lamb:
                if random.choices((True, False), (1 / n, 1 - (1 / n)))[0]:
                    list_y[idx] = str(1 - int(val))

        y = ''.join(list_y)
        if test_function(y) >= test_function(x):
            x = y
    return counter


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
    result = 0
    n = len(string)
    #-------------------------------------------------- k = random.randint(0, n)
    k = 3
    for char in string:
        result += int(char)
      
    if result < n-k or result == n:
        return result
    if result >= n-k and result < n:
        return n-k

def bin_val(string):
    return int(string, 2)


def royal_roads(string):
    result = 0
    n = len(string)
    #-------------------------------------------------- k = random.randint(1, n)
    k = 5
    if n%k == 0:
        lst = split_string(k, string)
        for element in lst:
            amount = 0
            for char in element:
                amount += int(char)
                if amount == k:
                    result += 1              
    return result        

runs = 25
print("OneMax: " + str(algorithm_rls(runs, one_max)))
print("leading_ones: " + str(algorithm_rls(runs, leading_ones)))
print("jump_k: " + str(algorithm_rls(runs, jump_k)))
print("bin_val: " + str(algorithm_rls(runs, bin_val)))
print("royal_roads: " + str(algorithm_rls(runs, royal_roads)))

print("OneMax: " + str(algorithm_11_ea(runs, one_max)))
print("leading_ones: " + str(algorithm_11_ea(runs, leading_ones)))
print("jump_k: " + str(algorithm_11_ea(runs, jump_k)))
print("bin_val: " + str(algorithm_11_ea(runs, bin_val)))
print("royal_roads: " + str(algorithm_11_ea(runs, royal_roads)))
