class Doors:
    doors = ['Закрыто']*4
    def Open(self,x):
        self.doors[x-1] = 'Открыто'
    def Close(self,x):
        self.doors[x-1] = 'Закрыто'

class Lights:
    def On(self):
        self.fari = 'ON'
        print('Turned ON')
    def Off(self):
        self.fari = 'OFF'
        print('Turned OFF')

class Cars(Doors, Lights):
    def __init__(self, color = None, model = None, kuzov = None, price = None, kpp= None, sost = None, god = None):
        self.fari = None
        self.color = color
        self.model = model
        self.kuzov= kuzov
        self.price = price
        self.kpp = kpp
        self.sost = sost
        self.god = god
    def carinfo(self):
        self.Open(3)
        print(self.doors)
    def save(self):
        for_save=str(self.color)+' '+str(self.model)+' '+str(self.kuzov)+' '+str(self.price)+' '+str(self.kpp)+' '+str(self.sost)
        self.for_save=for_save

class Interface():
    @staticmethod
    def read():
        f=open('car3')
        for s in f:
            m=s.split()
            massiv.append(Cars(m[0],m[1],m[2],m[3],m[4],m[5],m[6]))
    @staticmethod
    def Save():
        f=open('car3','w')
        for s in massiv:
            s.save()
            f.write(s.for_save+'\n')
        f.close()

    def __init__(self):
        self.UserInFace()
    def UserInFace(self):
        while True:
            print('_______________________')
            print('Введите номер действия')
            print('_______________________')
            print('1. Добавить автомобиль')
            print('2. Редактировать/взаимодействовать с автомобилем')
            print('3. Посмотреть всю информацию об автомобиле')
            print('4. Показать список автомобилей')
            print('5. Удалить автомобиль')
            print('6. Закончить')
            print('_______________________')
            a = input()
            if a == '1':
                print('Введите производителя и модель')
                massiv.append(Cars(model = input()))
                Interface.Save()
                print('Автомобиль добавлен')
            elif a == '2':
                print('Введите порядковый номер модели, которую вы хотите редактировать')
                for i in range(len(massiv)):
                    print(i+1,'. ',massiv[i].model, sep = '')
                i = int(input())-1
                print('_______________________')
                print('Выберите номер действия')
                print('_______________________')
                print('1. Изменить производителя и модель')
                print('2. Изменить кузов')
                print('3. Изменить цвет')
                print('4. Изменить стоимость')
                print('5. Изменить тип трансмиссии')
                print('6. Изменить состояние')
                print('7. Открыть/закрыть двери')
                print('8. Включить/выключить фары')
                print('9. Изменить год')
                print('0. Назад')
                print('_______________________')
                b = input()
                if b == '1':
                    print('Введите производителя и модель')
                    massiv[i].model = input()
                    Interface.Save()
                    print('Производитель и модель изменены')
                if b == '2':
                    print('Введите новый тип кузова')
                    massiv[i].kuzov = input()
                    Interface.Save()
                    print('Кузов изменен')
                if b == '3':
                    print('Введите цвет')
                    massiv[i].color = input()
                    Interface.Save()
                    print('Цвет изменен')
                if b == '4':
                    print('Введите стоимость')
                    massiv[i].price = int(input())
                    Interface.Save()
                    print('Стоимость обновлена')
                if b == '5':
                    print('Введите тип трансмиссии')
                    massiv[i].kpp = input()
                    Interface.Save()
                    print('Трансмиссия изменена')
                if b == '6':
                    print('Введите состояние автомобиля - Новая или Б/у')
                    massiv[i].sost=input()
                    Interface.Save()
                    print('Информация о состоянии автомобиля изменена')
                if b == '7':
                    print('Введите номер действия')
                    c = ''
                    while c != '0':
                        print(massiv[i].doors)
                        print('1. Открыть двери')
                        print('2. Закрыть двери')
                        print('0. Назад')
                        c = input()
                        if c == '1':
                            print('Введите номер двери')
                            massiv[i].Open(int(input()))
                        if c == '2':
                            print('Введите номер двери')
                            massiv[i].Close(int(input()))
                if b == '8':
                    c = ''
                    while c != '0':
                        print('1. Включить')
                        print('2. Выключить')
                        print('0. Назад')
                        c = input()
                        if c == '1':
                            massiv[i].On()
                        if c == '2':
                            massiv[i].Off()
                if b == '9':
                    print('Введите новый год')
                    massiv[i].god= input()
                    Interface.Save()
                    print('Год изменен')
                if b == '0':
                    k = Interface()
            elif a == '3':
                if len(massiv) == 0:
                    print('Нету доступных машин')
                else:
                    print('_______________________')
                    print('Выберите номер автомобиля, информацию о котором вы хотите получить')
                    print('_______________________')
                    for i in range(len(massiv)):
                        print(i+1,'. ',massiv[i].model, sep = '')
                    print('0. Назад')
                    i = int(input())-1
                    if i == -1:
                        a = Interface()
                    if massiv[i].model != None:
                        print('Производитель/Модель-', massiv[i].model)
                    if massiv[i].kuzov != None:
                        print('Кузов -', massiv[i].kuzov)
                    if massiv[i].color != None:
                        print('Цвет -', massiv[i].color)
                    if massiv[i].price != None:
                        print('Стоимость -', massiv[i].price)
                    if massiv[i].kpp != None:
                        print('Тип трансмиссии -', massiv[i].kpp)
                    if massiv[i].sost != None:
                        print('Состояние -', massiv[i].sost)
                    if massiv[i].fari != None:
                        print ('Фары -',massiv[i].fari)
                    if massiv[i].god != None:
                        print ('Год -',massiv[i].god)
                    print('Двери -',massiv[i].doors)
                    input()
            elif a == '4':
                if len(massiv) == 0:
                    print('Для начала добавьте автомобиль')
                else:
                    for i in range(len(massiv)):
                        print(i+1,'. ',massiv[i].model, sep = '')
            elif a == '5':
                if len(massiv) == 0:
                    print('Нет автомобилей')
                else:
                    for i in range(len(massiv)):
                        print(i+1,') ',massiv[i].model, sep = '')
                    c = int(input())
                    del massiv[i]
                    Interface.Save()
            elif a == '6':
                break
massiv = []
Interface.read()
a = Interface()
Interface.Save()