# TODO: запустить скрипт с параметрами, открыть и прочитать csv файл и проверить прочитанное содержание

import csv

def test_saved_bpi(name):
    count = 0
    with open(name, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(row)
            count +=1
    return count