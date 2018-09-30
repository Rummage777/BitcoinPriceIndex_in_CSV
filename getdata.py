import requests


def get_bpi_data(url, start, end):
    '''Function takes as arguments string: url address, begining of the period, ending of the period.
    Functions returns variable bpi_data, which conteins API response in json format (list of dict)'''
    arguments = {'start': start, 'end': end}
    bpi_data = requests.get(url, params=arguments, timeout=60)
    return bpi_data


