a = []
n = 1
b = {}
c = []
s_name = []
s_price = []
s_count = []
s_st = []
while True:

    name = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    count = input("Введите количество товара: ")
    st = input("Введите единицы измерения товара: ")
    bd = {'Название': name, "Цена": price, "Количество": count, "ед. изм": st}
    s_bd = {'Название': s_name, "Цена": s_price, "Количество": s_count, "ед. изм": s_st}
    a.append(n)
    a.append(bd)
    s_name.append(name)
    s_price.append(price)
    s_count.append(count)
    s_st.append(st)
    b = tuple(a)
    c.append(b)
    x = input("Для ввода следующего товара нажмите Enter\nДля окончания нажмите -\n")
    if x == '-':
        print(c)
        print(s_bd)
        break
    else:
        n += 1
