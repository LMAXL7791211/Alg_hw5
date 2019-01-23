#  2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
#  При этом каждое число представляется как массив, элементы которого это цифры числа.
#  Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#  Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


def dec_to_hex_list(dec):
    return list(hex(dec)[2:].upper())


def hex_list_to_dec(hex_list):
    accordance = [dec_to_hex_list(i)[0] for i in range(16)]
    return sum((accordance.index(a) * (16 ** (len(hex_list) - 1 - i)) for i, a in enumerate(hex_list)))


print("\nВведите шестнадцатеричные числа (используйте цифры 0-9 и латинские буквы A-F или a-f), без разделителей")
h1 = list(input('Введите первое число --> ').upper())
h2 = list(input('Введите второе число --> ').upper())

#  h1 = ['A', '2'] #  пример из задачи
#  h2 = ['C', '4', 'F']
print(f'Первое число = {h1}\nвторое = {h2}\n')

h1_dec = hex_list_to_dec(h1)
h2_dec = hex_list_to_dec(h2)

sum_dec = h1_dec + h2_dec
multiply_dec = h1_dec * h2_dec
# print(sum_dec, multiply_dec) #  для наглядности печатает результаты в десятичной системе

sum_hex = dec_to_hex_list(sum_dec)
multiply_hex = dec_to_hex_list(multiply_dec)
print(f'Сумма = {sum_hex} , произведение = {multiply_hex}\n')

print(f"{''.join(h1)} + {''.join(h2)} = {''.join(sum_hex)}")
print(f"{''.join(h1)} * {''.join(h2)} = {''.join(multiply_hex)}")
