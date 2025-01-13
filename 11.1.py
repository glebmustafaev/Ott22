import pandas as pd
import numpy as np
#С помощью Series(аналога словаря) мы можем упорядочить данные
s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print(s)
print()
#С помощью linspace мы можем выстроить последовательность чисел с одинаковым размером шага
s = pd.Series(np.linspace(0, 1, 5))
print(s)
#Также можно использовать arange. Но если мы берём числа типа float то мы можем получить не точный ответ
s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print("Фильтрация")
print(s[s > 2])
