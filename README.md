# User CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built with FastAPI and MongoDB. This project demonstrates a clean layered architecture using routes, services, repositories, schemas, and database modules.

## Features

* Create a new user
* Get all users
* Get a user by ID
* Update a user
* Delete a user
* Async MongoDB operations using Motor
* Environment variable configuration with dotenv

## Tech Stack

* FastAPI
* MongoDB
* Motor (Async MongoDB Driver)
* Pydantic
* Python 3.10+

## Project Structure

```text
app/
│
├── main.py
├── routes/
│   └── user_routes.py
├── services/
│   └── service.py
├── repositories/
│   └── user_repository.py
├── schema/
│   └── user_schema.py
├── db/
│   └── mongo.py
│
.env
requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
MONGO_URI=mongodb://localhost:27017
DB_NAME=testdb
```

### 5. Run MongoDB

Make sure MongoDB is running locally on port `27017`.

### 6. Start the application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Create User

```http
POST /users
```

Request Body:

```json
{
  "name": "prashanth",
  "email": "prashanth@example.com",
  "age": 22,
  "phone": "123457890",
  "address" : "random Address"
}
```

### Get All Users

```http
GET /users
```

### Get User By ID

```http
GET /users/{user_id}
```

### Update User

```http
PUT /users/{user_id}
```

Request Body:

```json
{
  "name": "Updated Name",
  "email": "updated@example.com",
}
### You can pass which field you want to update , what ever field you passed that will got updated
```
### Delete User

```http
DELETE /users/{user_id}
```

