#generation
from random import choice
direct = input('Введите директорию мозга:')
t = open(direct, 'r').read()
slow = eval(t)
a = input('Введите первое слово:')
sk = int(input('Введите сколько слов должно быть дописано:'))
p = a
for i in range(sk):
    if p in slow:
        k = choice(slow[p])
        a += ' ' + k
        p = k
    else:
        p = choice([i for i in slow])
        k = choice(slow[p])
        a += ' ' + k
        p = k
print(a)
