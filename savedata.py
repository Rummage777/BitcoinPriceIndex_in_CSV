
import csv
import datetime


def save_bpi_data(data, filename):
    '''Get dict with pairs: "Date: Price" and save it in csv file
    data contains dict: {'2018-11-09': 6545.76465}
    '''

    # Set headers for tabs
    tabs = ['Date', 'Price']

    # writing to csv file
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)

        # Writing headers
        # TODO: use method write header / Существует только для DictWriter, а он нам не подходит
        writer.writerow(tabs)

        # Writing the data rows
        for item in data.keys():
            row = []

            # Convert date from YYYY-MM-DD to DD.MM.YYYY output format
            date = [int(x) for x in item.split('-')]
            formatted_date = (datetime.date(date[0], date[1], date[2])).strftime("%d.%m.%y")
            row.append(formatted_date)

            # Convert price into $120.24 format
            price = data[item]
            price = '$' + str(format(price, '.2f'))
            row.append(price)

            # Write prepared line into csv file
            writer.writerow(row)

        print("Writing CSV file complete. Check current directory for new file named {}".format(filename))
