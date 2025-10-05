''' все буквы приводятся к нижнему регистру
    если в слове есть символ, не являющийся буквой,
    то эти символы просто удаляются из слова, так как
    в слове могут быть только буквы'''

a = input()
a = a.lower()
if a == '':
    print('Введите текст')
slova = a.split()
s_slova = set()
d_slova = {}
m_slova = []
symbol = '/.,!@#$^&*()_+=-]["№;%:?'
chisla = '1234567890'
m = 0
for el in slova:
    sl = ''
    for lett in el:
        if lett not in symbol and lett not in chisla:
            sl += lett
    s_slova.add(sl)
if len(s_slova) < 5:
    print('Введите минимум 5 разных слов')
    m = 1
if m == 0:
    for el in slova:
        sl = ''
        for lett in el:
            if lett not in symbol and lett not in chisla:
                sl += lett
        if sl in m_slova:
            b = d_slova[sl]
            d_slova[sl] = b + 1
        else:
            d_slova[sl] = 1
            m_slova.append(sl)
new_d = {k: v for k, v in d_slova.items() if k != ''}
sorted_d_slova = sorted(new_d.items(), key=lambda item: item[1], reverse=True)
c = sorted_d_slova[:5]
for el in c:
    print(el[0])

chisla = '1234567890'
symbol = '/.,!@#$^&*()_+=-]["№;%:?'
s_letter = set()
d_letter = {}
m_letter = []
m = 0
for el in slova:
    let = el.split()
    for el2 in let:
        for el3 in el2:
            if el3 not in chisla and el3 not in symbol:
                s_letter.add(el3)
if len(s_letter) < 5:
    print('Введите минимум 5 разных букв')
    m = 1
if m == 0:
    for el in slova:
        let = el.split()
        for el2 in let:
            for el3 in el2:
                if el3 in m_letter:
                    b = d_letter[el3]
                    d_letter[el3] = b + 1
                elif el3 not in chisla and el3 not in symbol:
                    d_letter[el3] = 1
                    m_letter.append(el3)
sorted_d_letter = sorted(d_letter.items(), key=lambda item: item[1], reverse=True)
n = sorted_d_letter[:5]
for el in n:
    print(el[0])
