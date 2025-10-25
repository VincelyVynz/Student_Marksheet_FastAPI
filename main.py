from fastapi import FastAPI
from database import engine, Base
from routers.students import  router as students_router

app = FastAPI(title= "Student Marksheet API")

# Create database tables
Base.metadata.create_all(bind = engine)

# include router
app.include_router(students_router, prefix="/students", tags=["Students"])

# Root
@app.get("/")
def read_root():
    return {"Message": "Welcome to Student Marksheet API!"}