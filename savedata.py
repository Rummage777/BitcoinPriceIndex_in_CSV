import csv


def save_bpi_data(response, filename):
    '''Get dict with pairs: "Date: Price" and save it in csv file'''

    # Clean response from odd info
    result = response['bpi']

    # Set headers for tabs
    tabs = ['Date', 'Price']

    # writing to csv file
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)

        # writing headers
        writer.writerow(tabs)

        # writing the data rows
        for item in list(result):
            a = []

            # Convert date from YYYY-MM-DD to DD.MM.YYYY output format
            date = list(reversed(item.split('-')))
            date = '.'.join(date)
            a.append(date)

            # Convert price into $120.24 format
            price = result[item]
            price = '$'+ str(format(price, '.2f'))
            a.append(price)

            # Write a line into csv
            writer.writerow(a)

    return filename
