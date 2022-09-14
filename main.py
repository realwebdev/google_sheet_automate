import gspread
from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
sa = gspread.service_account()
sh = sa.open('data_processing')
wks = sh.worksheet("data")
print('Rows: ', wks.row_count)
print('Rows: ', wks.col_count)

engine = create_engine('postgresql+psycopg2://admin:7410@localhost/algebra')


class Purchase(Base):
    __table_name__ = 'user_info'
    __table_args__ = {"schema": "lander"}

    phone_number = Column(Integer, primary_key=True)

