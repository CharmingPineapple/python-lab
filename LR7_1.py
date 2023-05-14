# Вариант 7.
# Создать матрицу случайных вещественных чисел 10×10. Числа в диапазоне от -5 до 5.
# Привести её к одномерному виду.

import numpy as np

A = np.random.uniform(-5, 5, (10, 10))
print("Матрица 10х10:\n", A)

listA_resh = A.reshape(1, 100)
listA_flat = A.flatten()

print("\nОдномерная матрица через reshape:\n", listA_resh)
print("\nОдномерная матрица через flatten:\n", listA_flat)