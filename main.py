import numpy as np

#1.    Створіть двовимірний масив 3x3 з випадкових цілих чисел від 1 до 100.

arr = np.random.randint(1, 101, size=(3, 3))
print(f"Масив:\n{arr}")

#2.    Обчисліть суму всіх елементів масиву.

total_sum = np.sum(arr)
print(f"\nЗагальна сума = {total_sum}")

#3.    Знайдіть максимальне та мінімальне значення в масиві, а також їхні індекси.
max_num = np.max(arr)
max_index = np.unravel_index(np.argmax(arr), arr.shape)

min_num = np.min(arr)
min_index = np.unravel_index(np.argmin(arr), arr.shape)

print(f'\nМаксимальне значення в масиві = {max_num}, його індекс = {max_index}')
print(f"Мінімальне значення в масиві = {min_num}, його індекс = {min_index}")

#4.    Відсортуйте масив по кожному рядку.

sorted_arr = np.sort(arr, axis=1)

print(f"\nВідсортований масив:")
print(sorted_arr)
