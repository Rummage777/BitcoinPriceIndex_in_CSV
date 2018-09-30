
import sys
import argparse
import getdata
import savedata
import tests


# Set API address
url = "https://api.coindesk.com/v1/bpi/historical/close.json"



def myAgrumentParser():
    '''Parser gets parameters from command line'''
    result = argparse.ArgumentParser(prog = 'BitcoinPriceIndex in CSV',
            description = '''Быстрое получение цены Bitcoin за произвольный период времени в csv формате.
            
            Чтобы задать собственные границы периода используйте аргументы:
            начало периода: -s или --start
            конец периода: -e или --end
            Формат даты: YYYY-MM-DD
            Пример: чтобы получить цену Bitcoin c 1 июля 2018 года по 10 июля 2018 года введите:
            python3 main.py -s 2018-07-01 -e 2018-07-10
            
              ''')
    result.add_argument('-s', '--start', type=str, default='2018-01-01')  # Beginning of the period
    result.add_argument('-e', '--end', type=str, default='2018-09-21')    # Ending of the period
    result.add_argument('-n', '--name', type=str, default='bpi')          # Set output CSV file name
    return result


if __name__ == '__main__':
    '''Ограничиваем запуск парсера модулем main и передаем значения в переменные Начало периода и Конец периода'''
    result = myAgrumentParser()
    arguments = result.parse_args(sys.argv[1:])
    start_data = arguments.start
    end_data = arguments.end
    filename = arguments.name + '.csv'

    # Используем модуль getdata, для получения данных и сохраняем полученный ответ как string в переменную getbpi
    getbpi = getdata.get_bpi_data(url, start_data, end_data)

    # Проверяем, что сервер ответил на запрос
    if getbpi.status_code == 200:
        bpi = savedata.save_bpi_data(getbpi.json(), filename)

    else:
        # Если сервер отдал статус отличный от ОК, останавливаем выполнение программы
        raise SystemExit("Invalid API response. Server answered {}. Try again later".format(getbpi.status_code))

# TODO: Сделать проверку, что файл записался и что файл не пустой
print("Csv file is ready. Check current directory for new file named {}".format(filename))

print('File has {} rows.'.format(tests.test_saved_bpi(filename)))
