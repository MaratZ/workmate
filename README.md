### CSV Processor
## Описание проекта
Этот скрипт предназначен для обработки CSV-файлов с возможностью фильтрации и агрегации данных. Проект разработан как тестовое задание для демонстрации навыков работы с Python.

## Основные функции:

Фильтрация данных с операторами: >, <, ==

Агрегация данных: вычисление среднего (avg), минимального (min) и максимального (max) значений

Поддержка работы как с числовыми, так и с текстовыми данными

Технологии и библиотеки
В проекте использованы:

## Стандартные библиотеки Python:

argparse - для обработки аргументов командной строки

csv - для работы с CSV-файлами

## Внешние библиотеки:

tabulate - для красивого вывода таблиц в консоль

pytest - для тестирования кода

## Установка и запуск
Клонируйте репозиторий:


git clone https://github.com/MaratZ/workmate.git
cd workmate
Установите зависимости:


pip install -r requirements.txt
Запуск скрипта:

## Примеры использования:


# Фильтрация: цена больше 500
python csv_processor.py data.csv --where "price=> 500"

# Агрегация: средний рейтинг
python csv_processor.py data.csv --aggregate "rating=avg"

# Комбинированный пример
python csv_processor.py data.csv --where "brand==apple" --aggregate "price=avg"
Тестирование
Для запуска тестов:


pytest test_csv_processor.py -v
Для проверки покрытия тестами:


pytest --cov=csv_processor test_csv_processor.py
Особенности реализации
Гибкая система фильтрации:

Поддержка различных форматов условий (>500, price>500, price=>500)

Работа с числами и строками

Учет регистра при сравнении строк

## Модульная архитектура:

Четкое разделение логики фильтрации и агрегации

Возможность легкого расширения функционала

## Полное покрытие тестами:

Тестирование всех основных сценариев работы

Проверка граничных случаев

Пример входных данных
Файл data.csv:

text
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4

![image](https://github.com/user-attachments/assets/b35a6978-f047-47fd-b3f7-4b4af6bd44d3)


