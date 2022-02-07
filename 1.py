''' Полотнянко вариант 17 решение линейного уравнения методом итерации '''

import time
import math

time.sleep(1) # очікування
print('Function is X^3 + 5x + 11') # первинна функція
time.sleep(1)
print('Lower bound is (-2)') # нижня межа діапазону який містить розв'язок
time.sleep(1)
print('Upper bound is (-1)') # верхня межа
time.sleep(1)
print('x = x - l(x^3 + 5X + 11)') # рівняння змінене для можливості застосування методу ітерації, лямбда дорівнює 1/20
time.sleep(1)
a2 = -1.5 # довільне значення від якого починаємо ітерацію
i = 0 # лічильник ітерацій
while(i<10):
    a2 = a2 - 0.05 * (a2**3 + 5*a2 + 11)
    i = i + 1
print('X =',a2)
time.sleep(3)