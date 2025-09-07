a = input()
if a == '':
    print('Введите текст')
slova = a.split()
s_slova = set()
d_slova = {}
m_slova = []
m = 0
for el in slova:
    s_slova.add(el)
if len(s_slova) < 5:
    print('Введите минимум 5 разных слов')
    m = 1
if m == 0:
    for el in slova:
        if el in m_slova:
            b = d_slova[el]
            d_slova[el] = b + 1
        else:
            d_slova[el] = 1
            m_slova.append(el)
sorted_d_slova = sorted(d_slova.items(), key=lambda item: item[1], reverse=True)
c = sorted_d_slova[:5]
for el in c:
    print(el[0])

chisla = '1234567890'
s_letter = set()
d_letter = {}
m_letter = []
m = 0
for el in slova:
    let = el.split()
    for el2 in let:
        for el3 in el2:
            if el3 not in chisla:
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
                elif el3 not in chisla:
                    d_letter[el3] = 1
                    m_letter.append(el3)
sorted_d_letter = sorted(d_letter.items(), key=lambda item: item[1], reverse=True)
n = sorted_d_letter[:5]
for el in n:
    print(el[0])
