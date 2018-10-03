# TODO: создать тесты
"""
Задание:
0) Описать запуск тестов в README
1) Каждый тест - отдельная функция
2) Тесты никогда не принимают аргументы
3) Тест №1: проверить, что первый попавшийся ключ в словаре в ответе API имеет нужный формат
4) Тест №2: создать данные вручную словарь, записать эти данные в файл и проверить,
что записались правильные данные
"""


import getdata
import savedata
from settings import URL
import csv

def test_dict_key():
    # Set test data
    passed = True
    start_data = '2018-01-01'
    end_data = '2018-01-05'
    expected_data = {'2018-01-01': 13412.44,
                     '2018-01-02': 14740.7563,
                     '2018-01-03': 15134.6513,
                     '2018-01-04': 15155.2263,
                     '2018-01-05': 16937.1738}

    result = getdata.get_bpi_data(URL, start_data, end_data)

    for item in result.keys():
        if type(item) is not str:
            passed = False
        if type(result[item]) is not float:
            passed = False
        if item not in expected_data:
            passed = False

    for item in expected_data.keys():
        if item not in result:
            passed = False

    if '2018-01-06' in result.keys():
        passed = False

    if result['2018-01-01'] != 13412.44:
        passed = False

    if passed == True:
        print("Test #1 successfully passed")
    else:
        print("Test #1 failed")


def test_writing_reading():

    # Set test data
    filename = 'test_data.csv'
    test_input = {'2018-01-01': 6545.76465,
                  '2018-01-02': 56445.76465,
                  '2018-01-03': 23145.76465}
    test_output = {'Date': 'Price',
                   '01.01.18': '$6545.76',
                   '02.01.18': '$56445.76',
                   '03.01.18': '$23145.76'}

    # Execute writing with test data
    savedata.save_bpi_data(test_input, filename)

    # Execute reading from CSV files. Takes lists, convert to dictionary and save to variable new_dict
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        new_dict = {}
        for row in csv_reader:
            key = row[0]
            new_dict[key] = row[1]
        if new_dict == test_output:
            print("Test #2 successfully passed")
        else:
            print("Test #2 failed")


test_dict_key()
test_writing_reading()