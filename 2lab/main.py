'''
все буквы приводятся к нижнему регистру
'''

s1 = input().lower()
s2 = input().lower()
symbols = '0123456789!@#$%^&*()_+=-/.,<>"'
if len(s1) == 0 or len(s2) == 0:
    print('Введите непустую строку')
else:
    string1 = ''
    string2 = ''
    for elem in s1:
        if elem not in symbols:
            string1 += elem
    for elem in s2:
        if elem not in symbols:
            string2 += elem
    d1 = {}
    d2 = {}
    for el1 in string1:
        if el1 not in d1:
            d1[el1] = 1
        else:
            d1[el1] += 1
    for el2 in string2:
        if el2 not in d2:
            d2[el2] = 1
        else:
            d2[el2] += 1
    sorted_d1 = sorted(d1.items(), key=lambda item: item[1], reverse=True)
    sorted_d2 = sorted(d2.items(), key=lambda item: item[1], reverse=True)
    was = []
    for el1 in sorted_d1:
        for el2 in sorted_d2:
            if el1[1] == el2[1] and el2[0] not in was:
                print(el1[0] + '=' + el2[0])
                was.append(el2[0])
                break
    print(len(sorted_d1), len(sorted_d2), len(was))
    if len(was) == 0:
        print('Букв, удовлетворяющих условию, нет. Частота встречаемости букв в',
              'первой строке не совпадает ни с одной частотой встречаемости букв во второй ')
    elif len(was) != len(sorted_d1) or len(was) != len(sorted_d2):
        print('Не у каждой буквы из одной строки есть буква из второй с такой же частотой встречаемости')
