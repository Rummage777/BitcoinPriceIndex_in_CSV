import requests


def get_bpi_data(url, start, end):
    '''Function takes as arguments string: url address, begining of the period, ending of the period.
    Functions returns variable bpi_data, which conteins API response in json format (list of dict)'''
    arguments = {'start': start, 'end': end}
    bpi_data = requests.get(url, params=arguments, timeout=60)

    # Check if server return valid response
    if bpi_data.status_code == 200:
        bpi_data = bpi_data.json() # Takes from response data in json format
        bpi_data = bpi_data['bpi'] # Clean response data from additional info
        return bpi_data
    else:
        # If server response with not 200 code
        raise Exception("Invalid API response. Server answered {}.Try again later".format(bpi_data.status_code))
