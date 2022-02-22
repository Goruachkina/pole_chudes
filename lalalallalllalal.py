vv = set() # множество введённых букв
ost = set() # множество оставшихся букв
vse = {'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'}
# old - переменные, по номерам соответствующие буквам в русском алфавите
# если old == 0, то буква ещё не вводилась
# если old == 1, то буква вводилась
old_01 = 0
old_02 = 0
old_03 = 0
old_04 = 0
old_05 = 0
old_06 = 0
old_07 = 0
old_08 = 0
old_09 = 0
old_10 = 0
old_11 = 0
old_12 = 0
old_13 = 0
old_14 = 0
old_15 = 0
old_16 = 0
old_17 = 0
old_18 = 0
old_19 = 0
old_20 = 0
old_21 = 0
old_22 = 0
old_23 = 0
old_24 = 0
old_25 = 0
old_26 = 0
old_27 = 0
old_28 = 0
old_29 = 0
old_30 = 0
old_31 = 0
old_32 = 0
old_33 = 0
b = '0000' # загаданное слово, буквы которого заменены спец. символом "0" (при отгадывании символ заменяется буквой)
print('Это игра поле чудес. Слово: название фильма ужасов с белой маской...')
print(b)
sh_pop = 0 # счётчик попыток
# основной цикл для игры
while b != 'крик':
    a = input()
    sh_pop += 1
    sim = 0 
    # если в конце цикла sim=0, то ввод не соответствует правилам (по 1 символу)
    # если в конце цикла sim=1, то буква отгадана
    # если в конце цикла sim=2, то буква уже была введена или отгадана ранее (повторный ввод)
    # если в конце цикла sim=3, то введённое целиком слово не верное
    # остальные значения переменной sim объясняются командой print в конце программы
    if len(a) == 1: # случай, в котором вводят 1 символ
        if a[0] == 'А' or a[0] == 'а':
            a = 'а' # изменение регистров (везде одинаковое)
            if old_01 == 0:
                sim = 1
            if old_01 == 1:
                sim = 2
            old_01 = 1
        if a[0] == 'Б' or a[0] == 'б':
            a = 'б'
            if old_02 == 0:
                sim = 1
            if old_02 == 1:
                sim = 2
            old_02 = 1
        if a[0] == 'В' or a[0] == 'в':
            a = 'в'
            if old_03 == 0:
                sim = 1
            if old_03 == 1:
                sim = 2
            old_03 = 1
        if a[0] == 'Г' or a[0] == 'г':
            a = 'г'
            if old_04 == 0:
                sim = 1
            if old_04 == 1:
                sim = 2
            old_04 = 1
        if a[0] == 'Д' or a[0] == 'д':
            a = 'д'
            if old_05 == 0:
                sim = 1
            if old_05 == 1:
                sim = 2
            old_05 = 1
        if a[0] == 'Е' or a[0] == 'е':
            a = 'е'
            if old_06 == 0:
                sim = 1
            if old_06 == 1:
                sim = 2
            old_06 = 1
        if a[0] == 'Ё' or a[0] == 'ё':
            a = 'ё'
            if old_07 == 0:
                sim = 1
            if old_07 == 1:
                sim = 2
            old_07 = 1
        if a[0] == 'Ж' or a[0] == 'ж':
            a = 'ж'
            if old_08 == 0:
                sim = 1
            if old_08 == 1:
                sim = 2
            old_08 = 1
        if a[0] == 'З' or a[0] == 'з':
            a = 'з'
            if old_09 == 0:
                sim = 1
            if old_09 == 1:
                sim = 2
            old_09 = 1
        if a[0] == 'И' or a[0] == 'и':
            a = 'и'
            if old_10 == 0:
                sim = 1
            if old_10 == 1:
                sim = 2
            old_10 = 1
        if a[0] == 'Й' or a[0] == 'й':
            a = 'й'
            if old_11 == 0:
                sim = 1
            if old_11 == 1:
                sim = 2
            old_11 = 1
        if a[0] == 'К' or a[0] == 'к':
            a = 'к'
            if old_12 == 0:
                sim = 1
            if old_12 == 1:
                sim = 2
            old_12 = 1
        if a[0] == 'Л' or a[0] == 'л':
            a = 'л'
            if old_13 == 0:
                sim = 1
            if old_13 == 1:
                sim = 2
            old_13 = 1
        if a[0] == 'М' or a[0] == 'м':
            a = 'м'
            if old_14 == 0:
                sim = 1
            if old_14 == 1:
                sim = 2
            old_14 = 1
        if a[0] == 'Н' or a[0] == 'н':
            a = 'н'
            if old_15 == 0:
                sim = 1
            if old_15 == 1:
                sim = 2
            old_15 = 1
        if a[0] == 'О' or a[0] == 'о':
            a = 'о'
            if old_16 == 0:
                sim = 1
            if old_16 == 1:
                sim = 2
            old_16 = 1
        if a[0] == 'П' or a[0] == 'п':
            a = 'п'
            if old_17 == 0:
                sim = 1
            if old_17 == 1:
                sim = 2
            old_17 = 1
        if a[0] == 'Р' or a[0] == 'р':
            a = 'р'
            if old_18 == 0:
                sim = 1
            if old_18 == 1:
                sim = 2
            old_18 = 1
        if a[0] == 'С' or a[0] == 'с':
            a = 'с'
            if old_19 == 0:
                sim = 1
            if old_19 == 1:
                sim = 2
            old_19 = 1
        if a[0] == 'Т' or a[0] == 'т':
            a = 'т'
            if old_20 == 0:
                sim = 1
            if old_20 == 1:
                sim = 2
            old_20 = 1
        if a[0] == 'У' or a[0] == 'у':
            a = 'у'
            if old_21 == 0:
                sim = 1
            if old_21 == 1:
                sim = 2
            old_21 = 1
        if a[0] == 'Ф' or a[0] == 'ф':
            a = 'ф'
            if old_22 == 0:
                sim = 1
            if old_22 == 1:
                sim = 2
            old_22 = 1
        if a[0] == 'Х' or a[0] == 'х':
            a = 'х'
            if old_23 == 0:
                sim = 1
            if old_23 == 1:
                sim = 2
            old_23 = 1
        if a[0] == 'Ц' or a[0] == 'ц':
            a = 'ц'
            if old_24 == 0:
                sim = 1
            if old_24 == 1:
                sim = 2
            old_24 = 1
        if a[0] == 'Ч' or a[0] == 'ч':
            a = 'ч'
            if old_25 == 0:
                sim = 1
            if old_25 == 1:
                sim = 2
            old_25 = 1
        if a[0] == 'Ш' or a[0] == 'ш':
            a = 'ш'
            if old_26 == 0:
                sim = 1
            if old_26 == 1:
                sim = 2
            old_26 = 1
        if a[0] == 'Щ' or a[0] == 'щ':
            a = 'щ'
            if old_27 == 0:
                sim = 1
            if old_27 == 1:
                sim = 2
            old_27 = 1
        if a[0] == 'Ъ' or a[0] == 'ъ':
            a = 'ъ'
            if old_28 == 0:
                sim = 1
            if old_28 == 1:
                sim = 2
            old_28 = 1
        if a[0] == 'Ы' or a[0] == 'ы':
            a = 'ы'
            if old_29 == 0:
                sim = 1
            if old_29 == 1:
                sim = 2
            old_29 = 1
        if a[0] == 'Ь' or a[0] == 'ь':
            a = 'ь'
            if old_30 == 0:
                sim = 1
            if old_30 == 1:
                sim = 2
            old_30 = 1
        if a[0] == 'Э' or a[0] == 'э':
            a = 'э'
            if old_31 == 0:
                sim = 1
            if old_31 == 1:
                sim = 2
            old_31 = 1
        if a[0] == 'Ю' or a[0] == 'ю':
            a = 'ю'
            if old_32 == 0:
                sim = 1
            if old_32 == 1:
                sim = 2
            old_32 = 1
        if a[0] == 'Я' or a[0] == 'я':
            a = 'я'
            if old_33 == 0:
                sim = 1
            if old_33 == 1:
                sim = 2
            old_33 = 1
        if a[0] == 'к' or a[0] == 'К':
            b = 'к' + b[1:]
            b = b[:3] + 'к'
        elif a[0] == 'р' or a[0] == 'Р':
            b = b[:1] + 'р' + b[2:]
        elif a[0] == 'и' or a[0] == 'И':
            b = b[:2] + 'и' + b[3:]
    elif len(a) == 4 and (a[0] != 'к' and a[0] != 'К') and (a[1] != 'р' and a[1] != 'Р') and (a[2] != 'и' and a[2] != 'И') and (a[3] != 'к' and a[3] != 'К'):
        sim = 3
    elif len(a) == 4 and (a[0] == 'к' or a[0] == 'К') and (a[1] == 'р' or a[1] == 'Р') and (a[2] == 'и' or a[2] == 'И') and (a[3] == 'к' or a[3] == 'К'):
        sim = 4
    elif len(a) != 1 and len(a) != 4:
        if a[0] != '!':
            sim = 5
        elif a == '!help': # случай, когда запрашивают команды
            sim = 6
            sh_pop -= 1
        elif a == '!vveden' or a == '!ostatok': # случай, когда запрашивают команду 
            # добавление букв в множество введённых букв (vv)
            if old_01 == 1:
                vv.add('а')
            if old_02 == 1:
                vv.add('б')
            if old_03 == 1:
                vv.add('в')
            if old_04 == 1:
                vv.add('г')
            if old_05 == 1:
                vv.add('д')
            if old_06 == 1:
                vv.add('е')
            if old_07 == 1:
                vv.add('ё')
            if old_08 == 1:
                vv.add('ж')
            if old_09 == 1:
                vv.add('з')
            if old_10 == 1:
                vv.add('и')
            if old_11 == 1:
                vv.add('й')
            if old_12 == 1:
                vv.add('к')
            if old_13 == 1:
                vv.add('л')
            if old_14 == 1:
                vv.add('м')
            if old_15 == 1:
                vv.add('н')
            if old_16 == 1:
                vv.add('о')
            if old_17 == 1:
                vv.add('п')
            if old_18 == 1:
                vv.add('р')
            if old_19 == 1:
                vv.add('с')
            if old_20 == 1:
                vv.add('т')
            if old_21 == 1:
                vv.add('у')
            if old_22 == 1:
                vv.add('ф')
            if old_23 == 1:
                vv.add('х')
            if old_24 == 1:
                vv.add('ц')
            if old_25 == 1:
                vv.add('ч')
            if old_26 == 1:
                vv.add('ш')
            if old_27 == 1:
                vv.add('щ')
            if old_28 == 1:
                vv.add('ъ')
            if old_29 == 1:
                vv.add('ы')
            if old_30 == 1:
                vv.add('ь')
            if old_31 == 1:
                vv.add('э')
            if old_32 == 1:
                vv.add('ю')
            if old_33 == 1:
                vv.add('я')
            sh_pop -= 1
            if a == '!ostatok': sim = 11
            if a == '!vveden': sim = 10
    if sim == 0 : print('Вы ввели символ не из русского алфавита. Попытаейтесь ещё')
    if sim == 1 and a[0] != 'к' and  a[0] != 'р' and a[0] != 'и' : print('Ну емае, такой буквы нет :(')
    if sim == 2 : print ('Буква ',a[0],' уже была')
    if sim == 3 : print('Вы ввели слово целиком, но оно не верное')
    if sim == 4: 
        print('Вы ввели слово целиком и угадали. Повезло :)')
        b = 'крик'
    if sim == 5 : print('Неправильный ввод: вводим либо 1 букву, либо слово из 4 букв')
    if sim == 6 : print('Есть команды: !help - список команд; !ostatok - оставшиеся буквы; !vveden - уже введённые буквы')
    if sim == 10: print('Введены буквы: ', vv)        
    if sim == 11: print('Вы ещё не вводили буквы: ', (vse - vv))
    if sim == 1 and (a[0] == 'к' or  a[0] == 'р' or a[0] == 'и') : print('Такая буква есть!')
    print(b)
print('Это типа победа, но приза нет :)')
print('Количество затраченных попыток: ',sh_pop)