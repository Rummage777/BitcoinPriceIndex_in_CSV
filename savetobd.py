from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import mysqldb

Base = declarative_base()


class BpiData(Base):
    __tablename__ = 'dateprice'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    price = Column(String)

    def __init__(self, date, price):
        self.date = date
        self.price = price

    def __repr__(self):
        return "<BpiData('%s','%s')>" % (self.date, self.price)


# Create table
Base.metadata.create_all(engine)

def write_bpidata_to_bd(data):
    connection = mysqldb.connect(user="root", dbname="bpibase", host="localhost")
    cursor = connection.cursor()
    for date, price in data.items():
        record = BpiData(date, price)
        session.add(record)
    cursor.close()
    conection.commit()
    connection.close()
