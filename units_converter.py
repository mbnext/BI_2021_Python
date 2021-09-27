# homework 2

# Для конвертера можно взять любые величины, но выберите что-то интереснее метров и километров.
# Например отсюда - https://www.axwap.com/kipia/docs/fizicheskie-velichiny/
# Сложность конвертера и количество величин для конвертации на ваш вкус

# собственно единицы измерения (пусть пока массы будут - v1), "input_unit": {"output_unit1": coeff1 = input/output1,
# "output_unit2": coeff2 = input/output2"}
# v2 - добавила единицы энергии
converter_dict = {"kg": {"kg": 1, "g": 1000, "mg": 1000000, "µg": 1000000000},
                  "g": {"g": 1, "kg": 0.001, "mg": 1000, "mcg": 1000000},
                  "mg": {"mg": 1, "kg": 0.000001, "g": 0.001, "mcg": 1000},
                  "mcg": {"mcg": 1, "mg": 0.001, "kg": 0.000000001, "g": 0.000001},
                  "q": {"q": 1, "kg": 100, "g": 100000, "mg": 100000000, "mcg": 100000000000},
                  "t": {"t": 1, "q": 10, "kg": 1000, "g": 1000000, "mg": 1000000000, "mcg": 1000000000000},
                  "ct": {"ct": 1, "g": 0.2},
                  "N": {"N": 1, "kg": 0.980665},
                  "stone": {"stone": 1, "g": 6350.29318, "kg": 6350.29318 / 1000},
                  "pound": {"pound": 1, "g": 453.59237},
                  "ounce": {"ounce": 1, "g": 28.349523125},
                  "dram": {"dram": 1, "g": 1.7718451953125},
                  "grain": {"grain": 1, "mg": 64.79891},
                  "J": {"J": 1, "kJ": 0.001, "MJ": 0.000001, "cal": 1 / 4.1868},
                  "kJ": {"kJ": 1, "J": 1000, "MJ": 0.001},
                  "MJ": {"MJ": 1, "kJ": 1000, "J": 1000000},
                  "cal": {"cal": 1, "J": 4.1868, "kcal": 0.001, "Mcal": 0.000001},
                  "kcal": {"kcal": 1, "cal": 1000, "Mcal": 0.001},
                  "Mcal": {"Mcal": 1, "cal": 0.000001, "kcal": 0.001}}


# проверка входных единиц измерения
def input_units_checker(i_units):
    check_res = True
    if i_units not in converter_dict.keys():
        print('Исходная единица измерения не поддерживается. Введите единицы измерения из списка: {units}; '
              'или воспользуйтесь другим конвертером'.format(units=', '.join(converter_dict.keys())))
        check_res = False
    return check_res


# проверка входного значения
def input_value_checker(i_value):
    check_res = True
    if i_value < 0:
        print('Введенное значение меньше 0, введите число, большее или равное 0')
        check_res = False
        # входное значение на тип не проверяем, т.к. там выпадает ошибка float, если что;
        # а вот на отрицательность проверим
    return check_res


# проверка конечного значения
def output_units_checker(i_units, o_units):
    check_res = True
    if o_units not in converter_dict[i_units].keys():
        print('Конечная единица измерения не поддерживается. Введите единицы измерения из списка: {units}; '
              'или воспользуйтесь другим конвертером'.format(units=', '.join(converter_dict[i_units].keys())))
        check_res = False
    return check_res


input_units = input(
    'Введите исходные единицы измерения из списка: {units}: '.format(units=', '.join(converter_dict.keys())))
i_u_ch_res = input_units_checker(input_units)

# сразу проверяем, есть ли такое значение в converter_dict, если нет, завершаемся
if i_u_ch_res == False:
    raise SystemExit(1)

input_value = float(input("Введите исходное значение (число): "))
i_v_ch_res = input_value_checker(input_value)

# сразу проверяем (в данном лсучае пока на положительность), если не проходим - завершаемся
if i_v_ch_res == False:
    raise SystemExit(1)

output_units = input('Введите конечные единицы измерения из списка: {units}: '
                     ''.format(units=', '.join(converter_dict[input_units].keys())))
o_u_ch_res = output_units_checker(input_units, output_units)

# сразу проверяем, есть ли такое значение в converter_dict[input_units], если нет - завершаемся
if o_u_ch_res == False:
    raise SystemExit(1)

output_value = None

if i_u_ch_res == False or i_v_ch_res == False or o_u_ch_res == False:
    print("Что-то пошло не так, описание см.выше")
else:
    output_value = input_value * converter_dict[input_units][output_units]
    print('{0} {1} = {2} {3}'.format(input_value, input_units, output_value, output_units))
