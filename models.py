from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, backref

from db import Base, engine

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String)
    address = Column(String)
    phone = Column(String)

    # Связь с Employee, добавлен back_populates для двунаправленной связи
    employees = relationship("Employee", back_populates="company", cascade="all, delete-orphan")

    def __repr__(self):
        return f'Company(id={self.id}, name={self.name})'


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id', ondelete='CASCADE'), nullable=False)
    name = Column(String, nullable=False)
    job = Column(String)
    phone = Column(String, unique=True)
    email = Column(String, unique=True)
    date_of_birth = Column(Date)

    # Связь с Company, back_populates для двунаправленной связи
    company = relationship("Company", back_populates="employees")

    # Связь с Payment
    payments = relationship("Payment", back_populates="employee", cascade="all, delete-orphan")

    def __repr__(self):
        return f'Employee(id={self.id}, name={self.name})'


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id', ondelete='CASCADE'), nullable=False)
    payment_date = Column(Date)
    ammount = Column(Integer)

    # Связь с Employee
    employee = relationship("Employee", back_populates="payments")

    def __repr__(self):
        return f"Payment(id={self.id}, date={self.payment_date})"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
