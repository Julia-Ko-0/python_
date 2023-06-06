
# class cars:
#     def __init__(self,color,model,owner) :
#         self.__color = color
#         self.model = model
#         self.owner = owner
#     def metod(self,modell):
#         if modell == 1 :
#             print(self.model)
        
# # обьект
# car_1 = cars("blu",3,"i")
# car_2 = cars("black",2,"mmmmmm")
# # print(car_1.owner,car_2__color)
# car_1.metod(1)



# class cars:
#     def __init__(color,model,owner) :
#         __color = color
#         _model = model
#         _owner = owner
#     def metod(self,modell):
#         if modell == 1 :
#             print(self.model)
        
# # обьект
# car_1 = cars("blu",3,"i")
# car_2 = cars("black",2,"mmmmmm")
# # print(car_1.owner,car_2__color)
# car_1.metod(1)


# Родительский класс
class Phone:

    # Инициализатор
    def __init__(self):
        self.is_on = False

    # Включаем телефон
    def turn_on(self):
        self.is_on = True

    # Если телефон включен, делаем звонок
    def call(self):
        if self.is_on:
            print('Making call...')
# tel = Phone()
# # dir(tel)
# tel.__init__()
# tel.turn_on()
# tel.call()
# наследование
class MobilePhone(Phone):

    # Добавляем новое свойство battery
    def __init__(self):
        super().__init__()
        self.battery = 0

# Заряжаем телефон на величину переданного значения
    def charge(self, num):
        self.battery = num
        print(f'Charging battery up to ... {self.battery}%')

my_phon = MobilePhone()
my_phon.turn_on()
my_phon.call()
my_phon.charge(50)