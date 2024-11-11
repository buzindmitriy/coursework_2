class Vacancy:
    """Класс с данными по вакансии"""

    __slots__ = ("__title", "__url", "__salary", "__description")

    def __init__(self, title: str, url: str, salary: float, description: str) -> None:
        self.__title = title
        self.__url = url
        self.__salary = self.__valid_salary(salary)
        self.__description = description

    @staticmethod
    def __valid_salary(salary):
        if salary is not None:
            return salary
        else:
            return 0.0

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def description(self):
        return self.__description

    def __lt__(self, other):
        """Метод сравнения вакансий з/п в меньшую сторону"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Метод сравнения вакансий з/п в большую сторону"""
        return self.salary > other.salary
