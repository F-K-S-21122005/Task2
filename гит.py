

f= open('Perepis.txt', 'r')

lst =[elem for elem in f]

cout = 0

personMin = int(input('Введите минимальное значение'))
personMax = int(input('Введите максимальное значение'))


for i in lst:
    st =i.split()
    date = st[3][6:10]
    if int(date) < 1978:
        cout += 1
        print(st[0])

print(cout)

print('----------')

for i in lst:
    st =i.split()
    date = st[3][6:10]
    if personMin <= int(date[2:]) <= personMax:
        cout += 1
        print(f'{st[0]} {st[1]} {st[2]}')



f.close()