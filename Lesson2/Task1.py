banks = {'SBER': 3.2, 'VTB': 2.4, 'ALFA': 4.92, 'PRIOR': 3.0}
money = float(input("Введите сумму, которую вы планируете положить под проценты: "))

sum_list = []
sum_dict = {}

for key, value in banks.items():
    sum_list.append(int(money * value / 100))
    sum_dict[key] = int(money * value / 100)

print("sum =", sum_list)
print("sum =", sum_dict)