my_st = input("Введите строку:")

print(f"Введена строка: {my_st}\n")

my_st_to_list = my_st.split()

n = 1
for i in my_st_to_list:
    print(f"{n}  -  {i[:10]} ")
    n += 1

