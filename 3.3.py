def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
value_list = [1, 'list', False]
value_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*value_list)
print_params(**value_dict)
value_list_2 = [54.32, True]
print_params(*value_list_2, 42)
