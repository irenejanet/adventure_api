from fastapi import FastAPI, HTTPException, status
from db import conn
from model import Product,Employee,PurchaseOrder,Department,Sales,Location,Currency
# Create FastAPI instance
app = FastAPI()

cursor = conn.cursor()


@app.get("/products/")
def get_products():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT ProductID, Name, Color, ListPrice FROM Production_Product")
        products = cursor.fetchall()
        cursor.close()
        return {"products": products}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/products/{product_id}")
def get_product(product_id: int):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT ProductID, Name, Color, ListPrice FROM Production_Product WHERE ProductID = %s", (product_id,))
        product = cursor.fetchone()
        cursor.close()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"product": product}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 

@app.post("/employees/")
def create_employee(employee: Employee):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Person_Person(FirstName, LastName, EmailPromotion) VALUES (%s, %s, %s)"
        values = (employee.FirstName, employee.LastName, employee.EmailPromotion)

        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        return {"message": "Employee created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/create_purchase_order/")
def  create_purchase_order(purchase_data: dict):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Purchasing_PurchaseOrderDetail (PurchaseOrderID, ProductID ) VALUES (%s, %s)"
        values = (purchase_data["PurchaseOrderID"], purchase_data["ProductID"])
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        return {"message": "Customer created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.put("/departments/{department_id}")
def update_department(department_id: int, name: str, group_name: str):
    try:
        cursor = conn.cursor()
        query = "UPDATE HumanResources_Department SET Name = %s, GroupName = %s WHERE DepartmentID = %s"
        values = (name, group_name, department_id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        return {"message": "Department updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.put("/stores/{store_id}")
def update_store(store_id: int, name: str, sales_person_id: int):
    try:
        cursor = conn.cursor()
        query = "UPDATE Sales_Store SET Name = %s, SalesPersonID = %s "
        values = (name, sales_person_id, store_id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        return {"message": "Store updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/currencies/{currency_name}")
def delete_currency(currency_name: str):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM Sales_Currency WHERE Name = %s"
        cursor.execute(query, (currency_name,))
        conn.commit()
        cursor.close()
        return {"message": "Currency with Name '{currency_name}' deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.delete("/locations/{location_id}")
def delete_location(location_id: int):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM Production_Location WHERE LocationID = %s"
        cursor.execute(query, (location_id,))
        conn.commit()
        cursor.close()
        return {"message": f"Location with LocationID {location_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))