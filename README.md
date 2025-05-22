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



