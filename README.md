# CSV-FILE-API
# Django REST API for CSV Upload and Validation

# Overview

This project implements a Django REST Framework (DRF) API endpoint that allows users to upload a CSV file containing user data. The API validates the data and saves valid records to the database while providing a summary of successes and errors.

---

# Features

- Accepts `.csv` file uploads via a POST API
- Validates:
  - `name`: Must be a non-empty string
  - `email`: Must be a valid email address (duplicates are skipped)
  - `age`: Must be an integer between 0 and 120
- Returns a JSON response summarizing:
  - Number of records successfully saved
  - Number of records rejected
  - Detailed validation errors for rejected records

---

## Requirements

- Python 3.x
- Django
- Django REST Framework
- Postman (for API testing)
- SQLite3 (used as the default database)

---
## Install dependencies:

pip install django
pip install djangorestframework

---

## Run migrations:

python manage.py makemigrations
python manage.py migrate

---

## Start the server:

python manage.py runserver

---
## Resources Used

Django REST Framework Documentation

Google for common issues and error resolutions

ChatGPT for doubt clarification (not for writing code)

---
![image](https://github.com/user-attachments/assets/794d512e-7a3d-412f-9c59-4fe643a8e002)

![image](https://github.com/user-attachments/assets/6e1aaa6b-240a-4dda-ad75-edb9958b8115)

{
    "saved": 3,
    "rejected": 5,
    "errors": [
        {
            "row": 4,
            "errors": {
                "name": [
                    "This field may not be blank."
                ],
                "age": [
                    "Age must be between 0 and 120."
                ]
            }
        },
        {
            "row": 5,
            "errors": {
                "email": [
                    "Enter a valid email address."
                ]
            }
        },
        {
            "row": 7,
            "errors": {
                "email": [
                    "user with this email already exists."
                ]
            }
        },
        {
            "row": 8,
            "errors": {
                "email": [
                    "Enter a valid email address."
                ],
                "age": [
                    "A valid integer is required."
                ]
            }
        },
        {
            "row": 9,
            "errors": {
                "email": [
                    "Enter a valid email address."
                ],
                "age": [
                    "A valid integer is required."
                ]
            }
        }
    ]
}


---

![image](https://github.com/user-attachments/assets/79580b8d-24cc-4174-b2ff-7e8d3954166a)
