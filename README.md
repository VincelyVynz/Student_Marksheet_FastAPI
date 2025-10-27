# Student Marksheet API

This is a simple RESTful API for managing a student marksheet, built with FastAPI and SQLAlchemy.

## Features

*   Create, Read, Update, and Delete (CRUD) operations for students.
*   Get a list of all students.
*   Get a specific student by their ID.
*   Update a student's information.
*   Delete a student from the marksheet.

## Technologies Used

*   **Python:** The core programming language.
*   **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
*   **SQLAlchemy:** The Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
*   **SQLite:** The database used to store the student data.

## Project Structure

```
.
├── crud.py
├── database.py
├── main.py
├── models.py
├── README.md
├── requirements.txt
├── routers
│   └── students.py
├── schemas.py
└── students.db
```

*   `main.py`: The entry point of the application.
*   `database.py`: Handles the database connection and session management.
*   `models.py`: Defines the SQLAlchemy models for the database tables.
*   `schemas.py`: Defines the Pydantic models for data validation and serialization.
*   `routers/students.py`: Contains the API endpoints for student-related operations.
*   `crud.py`: Contains the core CRUD functions.
*   `students.db`: The SQLite database file.
*   `requirements.txt`: A list of the Python packages required to run this project.

## API Endpoints

The following endpoints are available:

| Method | Path                | Description                  |
|--------|---------------------|------------------------------|
| GET    | /                   | Welcome message              |
| POST   | /students/          | Create a new student         |
| GET    | /students/          | Get a list of all students   |
| GET    | /students/{student_id} | Get a specific student by ID |
| PUT    | /students/{student_id} | Update a student's information|
| DELETE | /students/{student_id} | Delete a student             |

## Getting Started

### Prerequisites

*   Python 3.7+
*   pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/VincelyVynz/Student_Marksheet_FastAPI.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd Student_Marksheet_FastAPI
    ```
3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```
2.  Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## Example Usage

You can use a tool like `curl` or any API client to interact with the API.

### Create a Student

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '''{
  "name": "John Doe",
  "subject": "Math",
  "marks": 95
}'''
```
