"""
Тимофей готовит материал ко дню открытых дверей кафедры Теории чисел.
Тимофей расскажет про Основную теорему арифметики.
В соответствии с этой теоремой любое число раскладывается
на произведение простых множителей единственным образом — с точностью до их перестановки.
Например, число 8 можно представить как 2 * 2 * 2.
Число 50 — как 2 * 5 * 5 (или 5 * 5 * 2, или 5 * 2 * 5).
Три варианта отличаются лишь порядком следования множителей.
Разложение числа на простые множители называется факторизацией числа.
Факторизацию в уме делать сложно, поэтому помогите Тимофею написать программу.
"""

import sys

number = int(sys.stdin.readline().strip())
multipliers = []
d = 2
while d * d <= number:
    if number % d == 0:
        multipliers.append(d)
        number //= d
    else:
        d += 1
if number > 1:
    multipliers.append(number)

multipliers.sort()
print(" ".join(map(str, multipliers)))
