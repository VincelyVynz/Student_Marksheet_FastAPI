from sqlalchemy.orm import Session
from . import models, schemas


#  Create a student
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name = student.name,
        subject = student.subject,
        marks = student.marks
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Get all students
def get_students(db: Session):
    return db.query(models.Student).all()

# Get a student by id
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

# Update a student
def update_student(db: Session, student_id: int, updated_student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        return None
    db_student.name = updated_student.name
    db_student.subject = updated_student.subject
    db_student.marks = updated_student.marks
    db.commit()
    db.refresh(db_student)
    return db_student


# Delete a student
def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        return None
    db.delete(db_student)
    db.commit()
    return db_student

