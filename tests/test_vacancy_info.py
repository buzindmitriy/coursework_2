from src.vacancy_info import Vacancy


def test_vacancy_initialization(vacancy_data):
    vacancy = Vacancy(
        title=vacancy_data['name'],
        url=vacancy_data['alternate_url'],
        salary=vacancy_data['salary']['from'],
        description=vacancy_data['snippet']['responsibility']
    )
    assert vacancy.title == 'Программист Python'
    assert vacancy.url == 'https://example.com/vacancy/1'
    assert vacancy.salary == 100000
    assert vacancy.description == 'Разработка приложений'


def test_vacancy_salary_validation():
    vacancy = Vacancy(title='Тест', url='https://example.com', salary=None, description='Описание')
    assert vacancy.salary == 0.0  # Проверяем, что зарплата по умолчанию равна 0
