from fake_math import devide as dvf
from true_math import devide as dvt

result1 = dvf(69, 3)
result2 = dvf(3, 0)
result3 = dvt(49, 7)
result4 = dvt(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
-------------------------------------------
def devide(first, second):
    if second != 0:
        return first / second
    else:
        return 'Ошибка'
-----------------------------------------
from math import inf
def devide(first, second):
    if second != 0:
        return first / second
    else: return inf
