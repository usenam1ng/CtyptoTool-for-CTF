from PIL import Image

print('***CRYPTOTOOL***')                                                                                    
print('_________________')
print()

def caesar(s, x):
    alphabeten1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabeten2 = 'abcdefghijklmnopqrstuvwxyz'
    albhabetru1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    albhabetru2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    simv = "!#@$%^&*()_+-={}[]:';,./<>?"
    ch = '0123456789'
    if s[0] in albhabetru1 or s[0] in albhabetru2:
            alphabetmain1, alphabetmain2 = albhabetru1, albhabetru2
    elif s[0] in alphabeten1 or s[0] in alphabeten2:
        alphabetmain1, alphabetmain2 = alphabeten1, alphabeten2
    if x == 0:
        gg = len(alphabetmain1)
        flag = True
    else:
        gg = 1
        flag = False
    for ff in range(gg):
        if flag:
            x = ff
        itog = ''
        for i in s:
            if i.isupper():
                albhabet = alphabetmain1
            else:
                albhabet = alphabetmain2
            mesto = albhabet.find(i)
            new_mesto = mesto + x
            if new_mesto >= len(albhabet):
                new_mesto -= len(albhabet)
            if i in simv or i in ch:
                itog += i
            else:
                itog += albhabet[new_mesto]
        print('результат', itog)

        
def rsa():
    pass

print('Чтобы расшифровать шифр цезаря введите cas')
print('Чтобы расшифровать шифр RSA ввделите rsa')
print('Что бы расшифровать Visual Crpto введите vc')
print('Чтобы выйти введите quit')

a = input()

if a == 'quit':
    quit()

if a == 'cas':
    print('Вы знаете шаг шифровки? Введите yes / no')
    a = input()
    if a == 'yes':
        s = input('Введите строку ')
        sh = int(input('Введите шаг '))
        caesar(s, sh)
    elif a == 'no':
        s = input('Введите строку ')
        caesar(s, 0)
if a == 'vc':
    print('Введите полное название первой картинки')
    a1 = input()
    print('Введите полное название второй картинки')
    a2 = input()
    i1 = Image.open(a1)
    pix1 = i1.load()
    i2 = Image.open(a2)
    pix2 = i2.load()

    flag = Image.new("RGB", i1.size)
    flagpix = flag.load()
    for row in range(i1.size[1]):
        for col in range(i1.size[0]):
            flagpix[col, row] = (
                (pix1[col, row][0]+pix2[col, row][0]) % 256,
                (pix1[col, row][1]+pix2[col, row][1]) % 256,
                (pix1[col, row][2]+pix2[col, row][2]) % 256)

    flag.save("flag.png")
