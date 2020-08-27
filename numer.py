import math
import string as S
import sys
#import separator

print('''
                                                                 __                               
                                                                /  |                              
 _______   __    __  _____  ____    ______    ______    ______  $$ |  ______    ______   __    __ 
/       \ /  |  /  |/     \/    \  /      \  /      \  /      \ $$ | /      \  /      \ /  |  /  |
$$$$$$$  |$$ |  $$ |$$$$$$ $$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$ |/$$$$$$  |/$$$$$$  |$$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$/ $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |$$ \__$$ |$$ | $$ | $$ |$$$$$$$$/ $$ |      $$ \__$$ |$$ |$$ \__$$ |$$ \__$$ |$$ \__$$ |
$$ |  $$ |$$    $$/ $$ | $$ | $$ |$$       |$$ |      $$    $$/ $$ |$$    $$/ $$    $$ |$$    $$ |
$$/   $$/  $$$$$$/  $$/  $$/  $$/  $$$$$$$/ $$/        $$$$$$/  $$/  $$$$$$/   $$$$$$$ | $$$$$$$ |
                                                                              /  \__$$ |/  \__$$ |
                                                                              $$    $$/ $$    $$/ 
                                                                               $$$$$$/   $$$$$$/
                                                                               
                                                                               by nikjust08
''',)

kort1 = ("а", "и", "с", "ъ")
kort2 = ("б", "й", "т", "ы")
kort3 = ("в", "к", "у", "ь")
kort4 = ("г", "л", "ф", "э")
kort5 = ("д", "м", "х", "ю")
kort6 = ("е", "н", "ц", "я")
kort7 = ("ё", "о", "ч")
kort8 = ("ж", "п", "ш")
kort9 = ("з", "р", "щ")
print ("Введите Год")
BDYear = input()
BDYear = int(BDYear )
print ("Введите Месяц")
BDMonth = input()
BDMonth = int(BDMonth )
lim = 12
if BDMonth > lim:
    lim = 12
    print("Неверное число, проверьте исходные данные")
    input()
    os.abort()
print ("Введите День")
BDDay = int(BDDay )

#testingBD = (BDDay , BDMonth , BDYear)
#print (testingBD )
lim = 22

if BDDay > lim:
    lim = 22
    BDDay = BDDay - lim
    
lim = 12
if BDMonth > lim:
    lim = 12
    print("Неверное число, проверьте исходные данные")
    input()
    os.abort()
    

#print (BDDay)
#print (BDMonth)

form0 = BDDay - BDMonth
form1 = BDYear - BDDay
form2 = BDYear - BDMonth
if form0 < 0:
    form0 = form0 - form0 - form0

print ("Введите Имя")
name = input()
print ("Введите Фамилию")
Surname = input()
print ("Введите Отчество")
Patronymic = input()

name = name.lower()
Surname = Surname.lower()
Patronymic = Patronymic.lower()

namespl = list(name)
surnamespl = list(Surname)
patronymicspl = list(Patronymic)
i = 0
while i < len(namespl):
    if namespl[i] in kort1:
        namespl[i] = "1"
    if namespl[i] in kort2:
        namespl[i] = "2"
    if namespl[i] in kort3:
        namespl[i] = "3"
    if namespl[i] in kort4:
        namespl[i] = "4"
    if namespl[i] in kort5:
        namespl[i] = "5"
    if namespl[i] in kort6:
        namespl[i] = "6"
    if namespl[i] in kort7:
        namespl[i] = "7"
    if namespl[i] in kort8:
        namespl[i] = "8"
    if namespl[i] in kort9:
        namespl[i] = "9"

    i = i+1
il = 0
while il < len(surnamespl):
    if surnamespl[il] in kort1:
        surnamespl[il] = "1"
    if surnamespl[il] in kort2:
        surnamespl[il] = "2"
    if surnamespl[il] in kort3:
        surnamespl[il] = "3"
    if surnamespl[il] in kort4:
        surnamespl[il] = "4"
    if surnamespl[il] in kort5:
        surnamespl[il] = "5"
    if surnamespl[il] in kort6:
        surnamespl[il] = "6"
    if surnamespl[il] in kort7:
        surnamespl[il] = "7"
    if surnamespl[il] in kort8:
        surnamespl[il] = "8"
    if surnamespl[il] in kort9:
        surnamespl[il] = "9"

    il = il+1

im = 0
while im < len(patronymicspl):
    if patronymicspl[im] in kort1:
        patronymicspl[im] = "1"
    if patronymicspl[im] in kort2:
        patronymicspl[im] = "2"
    if patronymicspl[im] in kort3:
        patronymicspl[im] = "3"
    if patronymicspl[im] in kort4:
        patronymicspl[im] = "4"
    if patronymicspl[im] in kort5:
        patronymicspl[im] = "5"
    if patronymicspl[im] in kort6:
        patronymicspl[im] = "6"
    if patronymicspl[im] in kort7:
        patronymicspl[im] = "7"
    if patronymicspl[im] in kort8:
        patronymicspl[im] = "8"
    if patronymicspl[im] in kort9:
        patronymicspl[im] = "9"

    im = im+1

patronymicstr =  "".join(patronymicspl)
surnamestr = "".join(surnamespl)
namestr = "".join(namespl)
patronymicstr = int(patronymicstr)
surnamestr = int(surnamestr)
namestr = int(namestr)

allinone = int((namestr + surnamestr + patronymicstr) / 3)

BDBYear = str(BDYear)
fomaterYear = list(BDBYear)
i = 0
for i in range(0, len(fomaterYear)): 
    fomaterYear[i] = int(fomaterYear[i])
sumofyear = sum(fomaterYear)

allinone = str(allinone)
namelist = list(allinone)
i = 0
for i in range(0, len(namelist)): 
    namelist[i] = int(namelist[i])
namesum = sum(namelist)

i = 0
while 21 < namesum - 22:
    namesum - 22
form1 = sumofyear
if sumofyear > BDDay:
    form1 = sumofyear - BDDay
    
form2 = sumofyear
if sumofyear > BDMonth:
    form2 = sumofyear - BDMonth

print("ДР:", BDDay,".",BDMonth,".",sumofyear)
print("ОПВ:", form0)
print("ЗКУ:", form1)
print("ЭБ:", form2)
print("Число имени", namesum)

print("Нажмите enter Чтобы Продолжить")
input()

print("Выберите вид вычислений")
print("1.Деньги")
print("2.Здоровье")
print("3.Что-то еще")
while True:
    SelectorUse = input()

    if SelectorUse == "1":
        print(1)
        break
    elif SelectorUse == "2":
        print(2)
        break
    elif SelectorUse == "3":
        print(3)
        break
    else:
        print("Выберите вид вычислений")
        print("1.Деньги")
        print("2.Здоровье")
        print("3.Что-то еще")
        

