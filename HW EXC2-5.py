while True:
    n = input("Введите число для рейтинга: ")
    if n.isdigit() == False:
        print("Вы ввели некоректное значение")
        continue
    n = int(n)
    if n == 0:
        print("\nВы завершили программу.")
        break
    if "1234567890".find(str(n)) != -1:
        rt = [7, 5, 5, 5, 4, 2, 2, 1]
        print(rt)
        if rt.count(n) > 0:
            rt.insert((rt.index(n) + rt.count(n)), n)
            print(f"{rt}\n")
        else:
            for i in rt:
                if n > i:
                    rt.insert(rt.index(i), n)
                    print(f"{rt}\n")
                    break
