
import sys
import argparse
import datetime
from datetime import date
import getdata
import savedata
from settings import URL


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

    yesterday = date.today() - datetime.timedelta(days=1)

    result.add_argument('-s', '--start', type=str, default='2018-01-01')  # Beginning of the period
    result.add_argument('-e', '--end', type=str, default=yesterday)       # Ending of the period
    result.add_argument('-n', '--name', type=str, default='bpi')          # Set output CSV file name
    return result

def main():
    ''' Function gets parameters: file name, starting date, ending date
        Function calls process for getting end saving data in CSV file
    '''

    result = myAgrumentParser()
    arguments = result.parse_args(sys.argv[1:])
    start_data = arguments.start
    end_data = arguments.end
    filename = arguments.name + '.csv'

    # Use getdata module to get data from coindesk.com API
    bpidata = getdata.get_bpi_data(URL, start_data, end_data)

    # Use savedata module to create CSV file
    savedata.save_bpi_data(bpidata, filename)


if __name__ == '__main__':
    main()
