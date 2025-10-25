from pydantic import BaseModel, ConfigDict

class StudentBase(BaseModel):
    name: str
    subject: str
    marks: int

# Input model for POST (no id)
class StudentCreate(StudentBase):
    pass

# Response model (includes id)
class StudentRead(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)  # Pydantic V2 replacement for orm_mode
