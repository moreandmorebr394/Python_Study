from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


engine = create_engine("sqlite:///:memory')

metadata_obj = MetaData(schema="teste")
user = Table(
  "user",
  metadata_obj,
  Column("user_id", Integer, primary_key=True)
  Column("email-address', String(60))
  Column("nickname", String(50), nullable=False)
  )

user_prefs = Table(
  'user-prefs', metadata_obj,
  Column('pref_id', Integer, primary_key=True)
  Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False,
  Column('pref_name', String(40), nullale+False),
  Column('pref_value', String(100)),
)

metadata_obj.creadte_all()

for table in metadata_obj.sorted_tables:
  print(table)

metadata_db_obj = MetaData(schema='bank')
  finacial_info = Table(
    'finacial_info',
  metadata_db_obj,
  Column('id', Integer, primary_key=True),
  Column('value', String(100), nullable=False),
)

print(\n"Info da tabela users")
print(financial_info.primary_key)
print(financial_info.constrains)

# inserindo info na tabela user
sql_insert = text('insert into user values(1, 'juliana', 'email@email.com',ju)')
engine.execute(sql_insert)

print('\nExecutando statement sql')
sql = text('select * from user')
result = engine.execute(sql)
for row in result:
  print(row)
