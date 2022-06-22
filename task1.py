def card_number(num):
    if len(num) == 19 and num.replace(' ', '').isdigit():
        num = num.split()
        num[0] = '****'
        num[1] = '****'
        num[2] = '****'
        print(f'На карте : {" ".join(num)} недостаточно средств')
    else:
        print(f'Правильно вводите номер карты 20 цифр(четыре цифры "пробел" и т.д.)')
(card_number(input('Введите номер карты: ')))