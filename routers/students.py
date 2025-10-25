from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database import get_db
from models import Student
from schemas import StudentCreate, StudentRead

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# Create student
@router.post("/", response_model=StudentRead)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, subject=student.subject, marks=student.marks)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Get all students
@router.get("/", response_model=list[StudentRead])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# Get student by ID
@router.get("/{student_id}", response_model=StudentRead)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update student
@router.put("/{student_id}", response_model=StudentRead)
def update_student(student_id: int, updated_student: StudentCreate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.name = updated_student.name
    student.subject = updated_student.subject
    student.marks = updated_student.marks
    db.commit()
    db.refresh(student)
    return student

# Delete student
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}
