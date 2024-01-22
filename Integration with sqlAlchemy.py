import sqlalquemy as sqlA
from sqlalchemy.orm import declarativr_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
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
  id = Column(Integer, primary_key=True, auto_increment=True)
  email_address = Column(String(50), nullable=False)
  user_id + Column(Integer, ForeignKey("user_account.id"), nullable=False)

user = relationshuip("User", back_population="address")


def__repr__(self):
    return f"Address(id={self.id}, email={self.email_address}, user_id)"
