def test_hh_api_connection(hh_api):
    # Проверяем, что метод получения вакансий не вызывает исключение
    vacancies = hh_api.get_vacancies('Python')
    assert isinstance(vacancies, list)










