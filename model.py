from pydantic import BaseModel
# Models for request and response data

class Product(BaseModel):
    ProductID: int
    name: str
    ListPrice: float
    color: int


class Employee(BaseModel):
    FirstName: str
    LastName: str
    EmailPromotion: int

class PurchaseOrder(BaseModel):
    PurchaseOrderID: int
    ProductID: int


class Department(BaseModel):
    DepartmentID: int
    Name: str
    GroupName: str

class Sales(BaseModel):
    BusinessEntityID: int
    Name: str
    SalesPersonID: int

class Location(BaseModel):
    LocationID: int


class Currency(BaseModel):
    Currency_name: str