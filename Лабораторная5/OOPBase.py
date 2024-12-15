import abc
import doctest


class Vehicle(abc.ABC):
    """
    Абстрактный класс, описывающий транспортное средство.
    """

    def __init__(self, model: str, max_speed: float):
        """
        Создание и подготовка к работе объекта "Транспортное средство"

        :param model: Модель транспортного средства
        :param max_speed: Максимальная скорость транспортного средства

        Примеры:
        >>> car = Vehicle("Tesla Model S", 250)  # инициализация экземпляра класса
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть числом")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")

        self.model = model
        self.max_speed = max_speed

    @abc.abstractmethod
    def start_engine(self) -> None:
        """
        Запуск двигателя транспортного средства.

        Примеры:
        >>> car = Vehicle("Tesla Model S", 250)
        >>> car.start_engine()
        """
        ...

    @abc.abstractmethod
    def stop_engine(self) -> None:
        """
        Остановка двигателя транспортного средства.

        Примеры:
        >>> car = Vehicle("Tesla Model S", 250)
        >>> car.stop_engine()
        """
        ...


class Tree(abc.ABC):
    """
    Абстрактный класс, описывающий дерево.
    """

    def __init__(self, species: str, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева в метрах

        Примеры:
        >>> oak = Tree("Oak", 5.5)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть числом")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")

        self.species = species
        self.height = height

    @abc.abstractmethod
    def grow(self, meters: float) -> None:
        """
        Увеличивает высоту дерева на заданное количество метров.

        :param meters: Количество метров для роста

        Примеры:
        >>> oak = Tree("Oak", 5.5)
        >>> oak.grow(1.2)
        """
        ...

    @abc.abstractmethod
    def shed_leaves(self) -> None:
        """
        Опадание листьев у дерева.

        Примеры:
        >>> oak = Tree("Oak", 5.5)
        >>> oak.shed_leaves()
        """
        ...


class Website(abc.ABC):
    """
    Абстрактный класс, описывающий веб-сайт.
    """

    def __init__(self, domain: str, traffic: int):
        """
        Создание и подготовка к работе объекта "Веб-сайт"

        :param domain: Доменное имя сайта
        :param traffic: Количество посещений в месяц

        Примеры:
        >>> site = Website("example.com", 10000)
        """
        if not isinstance(domain, str):
            raise TypeError("Домен должен быть строкой")
        if not isinstance(traffic, int):
            raise TypeError("Трафик должен быть целым числом")
        if traffic < 0:
            raise ValueError("Трафик не может быть отрицательным")

        self.domain = domain
        self.traffic = traffic

    @abc.abstractmethod
    def update_content(self, new_content: str) -> None:
        """
        Обновляет контент на сайте.

        :param new_content: Новый контент для обновления

        Примеры:
        >>> site = Website("example.com", 10000)
        >>> site.update_content("New blog post")
        """
        ...

    @abc.abstractmethod
    def increase_traffic(self, amount: int) -> None:
        """
        Увеличивает количество посещений на заданное число.

        :param amount: Количество дополнительных посещений

        Примеры:
        >>> site = Website("example.com", 10000)
        >>> site.increase_traffic(500)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
