import sqlalquemy as sqlA
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect
from sqlalchemy import Integer
from sqlalchemy import ForeignKey


Base = declarative_base()


class User(Base):
  __tablename__ = "user_account"
  # atributos
  id = Column(Integer, primary_key=True)
  name = Column(String)
  fullname = Column(String)


address = relationship(
  "Address", back_populates="user", cascade="all, delete_orphan"
)

def __repr__(self):
    return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
  __tablename__ = "address"
  id = Column(Integer, primary_key=True)
  email_address = Column(String(50), nullable=False)
  user_id + Column(Integer, ForeignKey("user_account.id"), nullable=False)

user = relationship("User", back_populates="address")


def__repr__(self):
    return f"Address(id={self.id}, email_address={self.email_address))"

print(User.__tablename__)
print(Address.__tablename__)

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.reate_all(engine)

# depreciado - será removido em futuro release
# print(engine.table_name())

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
  Juliana = User(
      name="juliana",
      fullname="Juliana Mascarenhas"
      address=[Address(email_address="juliana@email.com")]
  )
   Sandy = User(
      name="sandy",
      fullname="Sandy Cardoso"
      address=[Address(email_address="sandy@email.com")
              Address(email_address="sandy@email.com")]

  patrick = User(name="patrick, fullname="Patrick Cardoso")

  # enviando para o BD ()
  
  session.add_all([juliana, sandy, patrick])

  session.commit()

  stmt = select(User).where(User.name.in_(["Juliana"]))
  for user in session.scalars(stmt):
    print(user)

  stmt_address = select(Address).where(Address.user_id.in_([2]))
  print("Recuperando os endereços de email de Sandy")
  for address in session.scalars(stmt_address):
    print(address)
    
  order_stmt = select(User).order_by(User.fullname.desc())
  print("Recuperando info de maneira ordenada")
  for result in session.scalars(order_stmt):
    print(result)

  stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
  for result in session.scalars(stmt_join):
    print(result)

  print(select(User.fullname, Address.email_address).join_from(Address, User)

  connection = engine.connect()
  results = connection.execute(stmt_join).fetchall()
  print("Executando statement a partir da connection")
  for result in results:
      print(result)

  
  stmt_count = select(func.count("*")).select_from(User)
  print("Total de instâncias em User")
  for result in session.scalars(stmt_count):
      print(result)
  
  

