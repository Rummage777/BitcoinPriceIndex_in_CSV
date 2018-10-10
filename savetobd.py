import sqlalchemy
import

def write_bpidata_to_bd(data):
    connection = dbapi.connect(user="root", dbname="bpibase", host="localhost")
    cursor = connection.cursor()
    for date, price in date.items():


    cursor.close()
    conection.commit()
    connection.close()

