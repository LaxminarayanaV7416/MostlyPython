# Lets conquer sqlalchemy for best ORM mapping


# lets try connecting to postgresql first by creating engine!
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
engine = create_engine('postgresql+psycopg2://lucky:123456789@localhost:5432/lucky')

# as per above check we have successfull tested the connection to database and its usccesful
# now lets try creating some table and see what happens

metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
    )

# >>> metadata.create_all(engine)
