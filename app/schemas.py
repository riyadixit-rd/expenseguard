from pydantic import BaseModel

class ExpenseCreate(BaseModel):

    employee_name: str

    amount: float

    category: str


class ExpenseResponse(BaseModel):

    id: int
    employee_name: str
    amount: float
    category: str
    status: str
    fraud_score: int

    class Config:

        from_attributes = True