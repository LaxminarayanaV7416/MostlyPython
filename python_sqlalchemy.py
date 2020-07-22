# Lets conquer sqlalchemy for best ORM mapping
import pandas as pd

# lets try connecting to postgresql first by creating engine!
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select, and_, or_, not_, text, func
engine = create_engine('postgresql+psycopg2://lucky:123456789@localhost:5432/lucky')

# as per above check we have successfull tested the connection to database and its usccesful
# now lets try creating some table and see what happens

conn = engine.connect()

metadata = MetaData()
iris = Table('iris', metadata,
    Column('id', Integer, primary_key=True),
    Column('sepal_length', Integer),
    Column('sepal_width', Integer),
    Column('petal_length', Integer),
    Column('petal_width', Integer),
    )


# Now we have defined a table and lets create the table
# >>> metadata.create_all(engine)

#now we have created the table 
# lets go and insert the data into the table
# we will use multiple insert statement
df = pd.read_csv('~/Desktop/iris.csv')
data = []
for i,j in df.iterrows():
    data.append({'sepal_length':j['sepal length (cm)'],
    'sepal_width':j['sepal width (cm)'],
    'petal_length':j['petal length (cm)'],
    'petal_width':j['petal width (cm)']})

# we have the data ready so lets try inserting the data to the database
# >>> conn.execute(iris.insert(),data)

# lets try to select the data from database using select 
select_query = select([iris])

#lets execute the query, in return we will get the result object which is an generator
result = conn.execute(select_query)
for i in result:
    # print(i)
    pass

# lets do some more advanced selections
# print(result.fetchone())  >>> gives us only one instance of the select

print(iris.columns.sepal_length) # accessing the columns names or 
print(iris.c.sepal_length) # or we can use the c instead of columns

# lets see advanced select query
select_query = select([iris.c.sepal_length, iris.c.sepal_width])
print(conn.execute(select_query).fetchone())

# lets see the where clause now
# NOTE we can use where clause multiple times by adding .where and going on
select_query = select([iris.c.sepal_length,iris.c['sepal_width']]).where(iris.c.petal_width==0)

for row in conn.execute(select_query):
    # print(row)
    pass

# now lets see how to use and_, or_, not_ in sqlalchemy
select_query = select([iris.c.sepal_length, iris.c.sepal_width])\
    .where(or_(iris.c.sepal_length==5, 
    iris.c.petal_width==1))

for row in conn.execute(select_query):
    # print(row)
    pass

# now lets see how to execute the text based queries
query = text("SELECT * FROM iris WHERE sepal_length=:value_1")
result = conn.execute(query, value_1 = 5)

# NOTE where ever you use the :variable_name its will become your keyword argument.
# and we have to replace that keyword argment in execution phase that is conn.execute 

for row in result:
    print(row)


# for joins please visit SQLALCHEMY.ORG and see sql alchemy core and expression language





####################################################################################
                                # SQLALCHEMY ORM
####################################################################################
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()

class Table_name(Base):
    __tablname__ = 'table_name_in_db'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return f'table_name_in_db with id {self.id} and name {self.name}'