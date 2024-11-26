def is_prime(func):
    def wrapper(*args, **kwargs):
        j = func(*args, **kwargs)
        sum_ = sum(args)
        x = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                x = x + 1
        if x <= 0:
            print('Простое')
        else:
            print('Составное')
        return j

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
