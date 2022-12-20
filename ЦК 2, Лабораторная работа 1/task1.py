import doctest


class Laptop:
    def __init__(self, code_laptop: str, Core_CPU: int, serial_model: str, price):
        if not isinstance(code_laptop, str):
            raise TypeError('Название ноутбука должно быть типа str')
        self.code_PC = code_laptop
        if Core_CPU <= 0:
            raise TypeError('Число ядер процессора больше нуля')
        self.Core_CPU = Core_CPU
        if not isinstance(serial_model, str):
            raise TypeError('Номер PC должен содержать буквы и цифры')
        self.serial_model = serial_model
        if price <= 0:
            raise TypeError('Цена ниже нуля не бывает')
        self.price = price

    def PC_sold(self):
        print('Нет в наличии')


class Printer:
    def __init__(self, code_printer: str, type_printer: str, price):
        if not isinstance(code_printer, str):
            raise TypeError('Название принтера должен быть типа str')
        self.code_printer = code_printer
        if not isinstance(type_printer, str):
            raise TypeError('Тип принтера должен быть типа str')
        self.type_printer = type_printer
        if not price > 0:
            raise ValueError('Цена принтера больше нуля')
        self.price = price


class Monitor:
    def __init__(self, code_monitor: str, screen_diagonal, type_monitor: str, price):
        if not isinstance(code_monitor, str):
            raise TypeError('Название монитора должена быть типа str')
        self.code_monitor = code_monitor
        if screen_diagonal <= 0:
            raise ValueError('Не может быть диагональ монитора меньше 0')
        if not isinstance(type_monitor, str):
            raise TypeError('Тип монитора должен быть типа str')
        self.type_monitor = type_monitor
        if not price > 0:
            raise ValueError('Цена монитора больше нуля')
        self.price = price


if __name__ == "__main__":
    Apple_Macbook_Pro_14 = Laptop('Apple Macbook Pro 14', 10, 'MKGP396/A', 1999)
    HP_LaserJet_Pro = Printer('HP LaserJet Pro M15w', 'Лазерный', 200)
    HUAWEI_MateView_GT_34 = Monitor('HUAWEI MateView GT 34', 34, 'Игровой', 200)

    doctest.testmod()
    pass
