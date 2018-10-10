
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
        writer.writerow(tabs)

        # Writing the data rows
        for date, price in data.items():
            row = []

            # Convert date from YYYY-MM-DD to DD.MM.YYYY output format
            # Вместо ручного парсинга использовать встроенную функцию datetime strptime
            nonformatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            formatted_date = nonformatted_date.strftime("%d.%m.%y")
            row.append(formatted_date)

            # Convert price into $120.24 format
            price = '$' + str(format(price, '.2f'))
            row.append(price)

            # Write prepared line into csv file
            writer.writerow(row)

        print("Writing CSV file complete. Check current directory for new file named {}".format(filename))
