# Arithmetic

#  1. Создать переменную item_1 типа integer.
#  2. Создать переменную item_2 типа integer.
item_1 = 5
item_2 = 66
#  3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
result_sum = item_1+item_2
#  4. Вывести result_sum в консоль.
print(result_sum)
#  5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
result_subtr = item_1-item_2
#  6. Вывести result_subtr в консоль.
print(result_subtr)
#  7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
result_multi = item_1*item_2
#  8. Вывести result_multi в консоль.
print(result_multi)
#  9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
result_exp = item_1 ** item_2
#  10. Вывести result_exp в консоль.
print(result_exp)
#  11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
import math
result_m_exp = pow(item_1,item_2)
#  12. Вывести result_m_exp в консоль.
print("result_m_exp =", result_m_exp)
#  13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item 
result_s_root = item_2 ** (0.5)
#  14. Вывести result_s_root в консоль.
print(result_s_root)
#  15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
result_m_s_root = math.sqrt(item_2)
#  16. Вывести result_m_s_root в консоль.
print(result_m_s_root)
#  17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
## Сделано в строке 25 вроде
#  18. Вывести result_mp_s_root в консоль.

#  19. Присвоить переменной item_1 odd значение
item_1_odd = 17 
#  20. Присвоить переменной item_2 even значение
item_2_even = 8
#  21. Создать переменную result_division в которой вы разделите item_1 на item_2.
result_divison = item_1_odd / item_2_even
#  22. Вывести result_division в консоль.
print(result_divison)
#  23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
result_m_floor = math.floor(result_divison)
#  24. Вывести result_m_floor в консоль.
print('Результат в меньшую сторону равен',result_m_floor)
#  25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
result_m_ceil = math.ceil(result_divison)
#  26. Вывести result_m_ceil в консоль.
print('Результат в большую сторону равен', result_m_ceil)
#  27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = int(result_divison)
#  28. Вывести result_int в консоль.
print("Округление через явное приведение равно", result_int)
#  29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss = item_1//item_2
#  30. Вывести result_no_division_loss в консоль.
print(result_no_division_loss)
#  31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2
#  32. Вывести result_division_loss в консоль.
print(result_division_loss)

# Дальше будет реализация через арифметические действия с присваиванием.

#  33. Создать переменную item_3 и присвоить ей целое число
item_3 = 10
#  34. Прибавить 10 к item_3 с присвоением.
item_3+=10
#  35. Вывести item_3 в консоль.
print(item_3)
#  36. Отнять 5 от item_3 с присвоением.
item_3-=5
#  37. Вывести item_3 в консоль.
print(item_3)
#  38. Умножить item_3 на 3 с присвоением.
item_3*=3
#  39. Вывести item_3 в консоль.
print(item_3)
#  40. Разделить item_3 на 2 с присвоением.
item_3/=2
#  41. Вывести item_3 в консоль.
print(item_3)
#  42. Возвести в степень 2 item_3 с присвоением.
item_3**=2
#  43. Вывести item_3 в консоль.
print(item_3)
#  44. Найти квадратный корень item_3 с присвоением.
item_3**= 0.5
#  45. Вывести item_3 в консоль.
print(item_3)
#  46. Присвоить остаток от деления item_3
item_3 %= 10
#  47. Вывести item_3 в консоль.
print(item_3)