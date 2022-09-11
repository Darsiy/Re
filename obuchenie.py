#obuchenie
import os
direct = input('Введите директорию с текстами:')
direct2 = input('Введите путь сохранения мозгов, а также название файла в формате txt:')
files = os.listdir(direct)
files = [direct + '/' + i for i in files]
texts = [open(i, 'r', encoding='utf-8').read().replace('\n', ' ').split(' ') for i in files]
slow = {0:[]}
for i in texts:
    p = i[0]
    for j in i[1:]:
        if p in slow:
            slow[p].append(j)
        else:
            slow[p] = [j]
        p = j
t = open(direct2, 'w')
t.write(str(slow))
t.close()
