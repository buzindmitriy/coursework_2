import pytest
from src.abs_api_class import HHAPI


@pytest.fixture
def hh_api():
    return HHAPI()


@pytest.fixture
def vacancy_data():
    return {
        'name': 'Программист Python',
        'alternate_url': 'https://example.com/vacancy/1',
        'salary': {'from': 100000},
        'snippet': {'responsibility': 'Разработка приложений'}
    }

@pytest.fixture
def filename(tmp_path):
    return tmp_path / "test_vacancies.json"