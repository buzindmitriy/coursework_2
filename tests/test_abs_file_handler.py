import json

from src.json_holder import JSONFileHandler


def test_load_data(filename):
    test_data = [
        {'title': 'Тестовая вакансия 1', 'url': 'https://example.com/vacancy/1', 'salary': 50000,
         'description': 'Описание 1'},
        {'title': 'Тестовая вакансия 2', 'url': 'https://example.com/vacancy/2', 'salary': 60000,
         'description': 'Описание 2'}
    ]

    with open(filename, 'w') as f:
        json.dump(test_data, f)
    file_handler = JSONFileHandler(filename=str(filename))
    loaded_data = file_handler.load_data()
    assert loaded_data == test_data  # Проверяем, что загруженные данные совпадают с тестовыми данными


def test_save_data(filename):
    file_handler = JSONFileHandler(filename=str(filename))
    test_data = [
        {'title': 'Тестовая вакансия 1', 'url': 'https://example.com/vacancy/1', 'salary': 50000,
         'description': 'Описание 1'}
    ]
    file_handler.save_data(test_data)
    loaded_data = file_handler.load_data()
    assert len(loaded_data) == 1  # Проверяем, что данные сохранены
    assert loaded_data[0]['title'] == 'Тестовая вакансия 1'
    # Сохраняем дубликат
    duplicate_data = [
        {'title': 'Тестовая вакансия 1', 'url': 'https://example.com/vacancy/1', 'salary': 50000,
         'description': 'Описание 1'}
    ]
    file_handler.save_data(duplicate_data)
    loaded_data = file_handler.load_data()
    assert len(loaded_data) == 1  # Проверяем, что дубликаты не сохранены


def test_delete_data(filename):
    file_handler = JSONFileHandler(filename=str(filename))
    test_data = [
        {'title': 'Тестовая вакансия 1', 'url': 'https://example.com/vacancy/1', 'salary': 50000,
         'description': 'Описание 1'},
        {'title': 'Тестовая вакансия 2', 'url': 'https://example.com/vacancy/2', 'salary': 60000,
         'description': 'Описание 2'}
    ]
    file_handler.save_data(test_data)
    # Удаляем первую вакансию
    file_handler.delete_data({'title': 'Тестовая вакансия 1'})
    loaded_data = file_handler.load_data()
    assert len(loaded_data) == 1  # Проверяем, что осталась только одна вакансия
    assert loaded_data[0]['title'] == 'Тестовая вакансия 2'  # Проверяем, что это именно вторая вакансия
    # Удаляем вторую вакансию
    file_handler.delete_data({'title': 'Тестовая вакансия 2'})
    loaded_data = file_handler.load_data()
    assert len(loaded_data) == 0  # Проверяем, что данные удалены


def test_load_data_file_not_found(filename):
    file_handler = JSONFileHandler(filename=str(filename))
    data = file_handler.load_data()
    assert data == []  # Если файл не найден, возвращаем пустой список
