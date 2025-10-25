from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database import get_db
from models import Student
from schemas import StudentCreate, Student
from schemas import Student as StudentSchema

router = APIRouter(
    prefix = "/students", # All routes in this file will start with /students
    tags = ["students"]   # For automatic grouping in the Swagger docs
)


# create student endpoint
@router.post("/", response_model = StudentSchema)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name = student.name, subject = student.subject, marks = student.marks)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Get all students
@router.get("/", response_model = list[StudentSchema])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

# Get student by ID
@router.get("/{student_id}", response_model = StudentSchema)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student