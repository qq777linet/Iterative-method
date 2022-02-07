''' Полотнянко вариант 17 решение трансцедентного уравнения методом итерации '''
''' синус рахував з радіан '''
import time
import math

time.sleep(1) # очікування
print('Function is 4,33sin.4x-3,5x') # первинна функція
time.sleep(1)
print('Lower bound is (-1)') # нижня межа діапазону який містить розв'язок
time.sleep(1)
print('Upper bound is (1)') # верхня межа
time.sleep(1)
print('φ(x) = 4,33sin4X/3,5') # фі від ікса 
time.sleep(1)
a2 = 0.5 # довільне значення від якого починаємо ітерацію
i = 0 # лічильник ітерацій
while(i<100):
    a2 = 4.33 *math.sin(4*a2)/3.5
    i = i + 1
print('X =',a2)
time.sleep(3)
