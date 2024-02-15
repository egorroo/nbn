import random
import time
a = random.randint(1, 500)
start = time.time()
print('Спробуй вгадати число від 1 до 500 (в тебе 20 попиток, нуль це закінчити)\n\n')
for i in range(1, 21):
    c = int(input('Напиши число: '))
    if a == 0:
        print('Ти Вийшов!')
        print(i, 'спроб')
        end = time.time()
        print("Пройшло", end - start, 'секунд')
        break
    if c == a:
        print('Ти Вгадав!')
        print('За', i, 'спроб')
        end = time.time()
        rounded_number = round(end - start)
        print("Пройшло", rounded_number, "секунд")
        break
    if c < a:
        print('Холодно🥶')
    if c > a:
        print('Гарячо🥵')


