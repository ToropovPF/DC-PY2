import doctest


class Auto:
    def __init__(self, brand: str, model: str, release_year: int, price: float, power: int):
        """
            Создание и подготовка к работе объекта "Автомабили"
            :param brand: Марка автомобиля
            :param model: Модель автомобиля
            :param release_year: Год выпуска авто
            :param price: Цена авто в млн.руб
            :param power: Мощность автомобиля
            Примеры:
        >>> auto = Auto("Hyundai", "Solaris", 2022, 1.5, 123)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка машины должна быть типа str")
        self.brand = brand
        if not isinstance(model, str):
            raise TypeError("Марка машины должна быть типа str")
        self.model = model
        if not isinstance(release_year, int):
            raise TypeError("Год выпуска машины должна быть типа int")
        self.release_year = release_year
        if not isinstance(price, float):
            raise TypeError("Цена машины должна быть типа float")
        self.price = price
        if not isinstance(power, int):
            raise TypeError("Мощность должна быть типа int")
        if power <= 0:
            raise ValueError("Мощность должна быть положительным числом")
        self.power = power

    def __str__(self):
        return f"{self.brand} {self.model} {self.release_year} года," \
               f" мощностью {self.power} л.с. стоит {self.price} млн.руб"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, " \
               f"release_year={self.release_year!r}, price={self.price!r}, power={self.power!r})"

    def changes_prise(self, new_price: float):
        """
        Метод изменяет цену автомобиля
        :return: Новая цена автомобиля

        Пример:
        >>> auto = Auto("Hyundai", "Solaris", 2022, 1.6, 123)
        >>> auto.changes_prise(1.7)
        """
        if not isinstance(new_price, float):
            raise TypeError("Цена машины должна быть типа float")
        self.price = new_price

    def tuning(self, hp_plus: int):
        """
        Метод прибавляет мощности автомобилю
        :param hp_plus: Прибавляемая мощность
        :return: Изменённая мощность автомобиля

        Примерж:
        >>> auto = Auto("Hyundai", "Solaris", 2022, 1.6, 123)
        >>> auto.tuning(20)
        """
        if not isinstance(hp_plus, int):
            raise TypeError("Мощность должна быть типа int")
        if hp_plus <= 0:
            raise ValueError("Мощность должна быть положительным числом")
        self.power += hp_plus


class PassengerAuto(Auto):
    def __init__(self, brand: str, model: str, release_year: int, price: float, power: int, acceleration_to_100: float):
        """
            Создание и подготовка к работе дочернего класса "Легковой авомобиль"
            В данном классе были перегружены методы str и repr (добавлены новые атрибуты дочернего класса
            В дочернем классе появляется новый параметр
            :param brand: Марка автомобиля
            :param model: Модель автомобиля
            :param release_year: Год выпуска авто
            :param price: Цена авто в млн.руб
            :param power: Мощность автомобиля
            :param acceleration_to_100: Время от 0 до 100 км/ч
            Примеры:
        >>> auto = PassengerAuto("Hyundai", "Solaris", 2022, 1.6, 123, 11.5)
         """
        super().__init__(brand, model, release_year, price, power)

        if not isinstance(acceleration_to_100, float):
            raise TypeError("Время от 0 до 100 км/ч str")
        if acceleration_to_100 <= 0:
            raise ValueError("Время больше нуля")
        self.acceleration_to_100 = acceleration_to_100

    def tuning(self, hp_plus: int):
        """
            Перегруженный метод "tuning" из материнского класса "Cars",
             при повышении мощноности у легкового авто уменьшается время разгона
            :param hp_plus: Прибавляемая мощность
            :return: Новая мощность и новый разгон до 100
            Пример:
        >>> auto = PassengerAuto("Hyundai", "Solaris", 2022, 1.6, 123, 11.5)
        >>> auto.tuning(50)
            """
        if not isinstance(hp_plus, int):
            raise TypeError("Мощность должна быть типа int")
        if hp_plus <= 0:
            raise ValueError("Мощность должна быть положительным числом")
        self.power += hp_plus
        self.acceleration_to_100 -= round((hp_plus / 50), 1)  # каждые 50 л.c уменьшают на 1 секунду разгон до 100

    def __str__(self):
        return f"{self.brand} {self.model} {self.release_year} года мощностью {self.power} л.с. едет до 100 км/ч за " \
               f"{self.acceleration_to_100} секунды и стоит {self.price} млн.руб"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, " \
               f"release_year={self.release_year!r}, price={self.price!r}, power={self.power!r}," \
               f" acceleration_to_100={self.acceleration_to_100!r})"


class Truck_cars(Auto):
    def __init__(self, brand: str, model: str, release_year: int, price: float, power: int,
                 load_capacity: (int, float)):
        """
        Создание и подготовка дочернего "Автомобили" класса "Грузовые автомобили"
        В данном классе были перегружены методы str и repr (добавлены новые атрибуты дочернего класса)
        :param brand: Марка грузовика
        :param model: Серия грузовика
        :param release_year: Год выпуска
        :param price: Цена в млн.руб
        :param power: Мощность грузовика
        :param load_capacity: Грузоподъёмность (тонн)

        Пример:
        >>> truck_cars_1 = Truck_cars("Man", "TGX", 2010, 5.0, 450, 20)
        """
        super().__init__(brand, model, release_year, price, power)

        if not isinstance(load_capacity, (int, float)):
            raise TypeError("Грузоподъёмность должна быть типа int или float")
        if load_capacity <= 0:
            raise ValueError("Грузоподъёмность должна быть положительным числом")
        self.load_capacity = load_capacity

    def tuning(self, hp_plus: int):
        """
        Перегруженный метод "tuning" из материнского класса "Cars",
         при повышении мощноности у грузового автомобиля также должна и возрастать грузоподъёмность

        :param hp_plus: Прибавляемая мощность
        :return: Новая мощность и новая грузоподъёмность

        Пример:
        >>> Car_2 = Truck_cars("Man", "TGX", 2010, 5.0, 450, 20)
        >>> Car_2.tuning(100)
        """

        if not isinstance(hp_plus, (int, float)):
            raise TypeError("Мощность должна быть типа int или float")
        if hp_plus <= 0:
            raise ValueError("Мощность должна быть положительным числом")
        self.power += hp_plus
        self.load_capacity += (hp_plus * 0.04)

    def __str__(self):
        return f"{self.brand} {self.model} {self.release_year} года мощностью {self.power} л.с. грузоподъёмность " \
               f"{self.load_capacity} тонн и стоит {self.price} млн.руб"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, " \
               f"release_year={self.release_year!r}, price={self.price!r}, power={self.power!r}, " \
               f"load_capacity={self.load_capacity!r})"


if __name__ == "__main__":
    doctest.testmod()

    Car_0 = Auto("Hyundai", "Solaris", 2022, 1.5, 123)
    print(Car_0)
    print(repr(Car_0))
    Car_0.changes_prise(1.6)
    print(Car_0)

    Car_1 = PassengerAuto("Hyundai", "Solaris", 2022, 1.5, 123, 11.5)
    print(Car_1)
    print(repr(Car_1))
    Car_1.tuning(50)
    print(Car_1)

    Car_2 = Truck_cars("Man", "TGX", 2010, 5.0, 450, 20)
    print(Car_2)
    print(repr(Car_2))
    Car_2.tuning(100)
    print(Car_2)
