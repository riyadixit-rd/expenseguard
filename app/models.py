from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Expense(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    employee_name = Column(String, index=True)

    amount = Column(Float)

    category = Column(String)

    status = Column(String, default="Normal")

    fraud_score = Column(Integer, default=0)