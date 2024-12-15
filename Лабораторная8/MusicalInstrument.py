class MusicalInstrument:
    """
    Базовый класс для музыкальных инструментов.
    """
    def __init__(self, name: str, manufacturer: str):
        """
        Инициализация музыкального инструмента.

        :param name: Название инструмента.
        :param manufacturer: Производитель инструмента.
        """
        self._name = name  # Название инструмента
        self._manufacturer = manufacturer  # Производитель

    @property
    def name(self) -> str:
        return self._name

    @property
    def manufacturer(self) -> str:
        return self._manufacturer

    def __str__(self) -> str:
        return f"{self.name} от {self.manufacturer}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, manufacturer={self.manufacturer!r})"

    def play_sound(self) -> None:
        """
        Воспроизведение звука. Метод должен быть переопределён в дочерних классах.
        """
        raise NotImplementedError("Метод должен быть переопределён в дочерних классах")


class StringInstrument(MusicalInstrument):
    """
    Дочерний класс для струнных инструментов.
    """
    def __init__(self, name: str, manufacturer: str, number_of_strings: int):
        """
        Инициализация струнного инструмента.

        :param name: Название инструмента.
        :param manufacturer: Производитель инструмента.
        :param number_of_strings: Количество струн.
        """
        super().__init__(name, manufacturer)
        self._number_of_strings = number_of_strings  # Количество струн

    @property
    def number_of_strings(self) -> int:
        return self._number_of_strings

    def __str__(self) -> str:
        return f"{self.name} ({self.number_of_strings} струн) от {self.manufacturer}"

    def play_sound(self) -> None:
        """
        Воспроизведение звука струнного инструмента.

        Этот метод переопределён для специфичного поведения струнных инструментов.
        """
        print(f"{self.name} издаёт мелодичный звук за счёт вибрации струн.")

    def tune_strings(self) -> None:
        """
        Настройка струн.
        """
        print(f"Настройка {self.number_of_strings} струн у {self.name}.")


class WindInstrument(MusicalInstrument):
    """
    Дочерний класс для духовых инструментов.
    """
    def __init__(self, name: str, manufacturer: str, material: str):
        """
        Инициализация духового инструмента.

        :param name: Название инструмента.
        :param manufacturer: Производитель инструмента.
        :param material: Материал, из которого изготовлен инструмент.
        """
        super().__init__(name, manufacturer)
        self._material = material  # Материал духового инструмента

    @property
    def material(self) -> str:
        return self._material

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, manufacturer={self.manufacturer!r}, material={self.material!r})"

    def play_sound(self) -> None:
        """
        Воспроизведение звука духового инструмента.

        Этот метод переопределён для специфичного поведения духовых инструментов.
        """
        print(f"{self.name} издаёт звук за счёт потока воздуха, проходящего через {self.material}.")

    def clean_instrument(self) -> None:
        """
        Чистка духового инструмента.
        """
        print(f"Чистка духового инструмента {self.name}.")


if __name__ == "__main__":
    # Примеры использования
    guitar = StringInstrument(name="Гитара", manufacturer="Yamaha", number_of_strings=6)
    flute = WindInstrument(name="Флейта", manufacturer="Yamaha", material="металл")

    print(guitar)         # Гитара (6 струн) от Yamaha
    print(repr(guitar))   # StringInstrument(name='Гитара', manufacturer='Yamaha', number_of_strings=6)
    guitar.play_sound()   # Гитара издаёт мелодичный звук за счёт вибрации струн.
    guitar.tune_strings() # Настройка 6 струн у Гитара.

    print(flute)          # Флейта от Yamaha
    print(repr(flute))    # WindInstrument(name='Флейта', manufacturer='Yamaha', material='металл')
    flute.play_sound()    # Флейта издаёт звук за счёт потока воздуха, проходящего через металл.
    flute.clean_instrument()  # Чистка духового инструмента Флейта.
