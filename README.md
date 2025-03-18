# Flask Users API 📄 

A simple REST API for managing users built with Flask and SQLAlchemy.
![123123123123](https://github.com/user-attachments/assets/0f51e84b-b6fe-4ada-840a-df027ca26d1a)

## Features ✨

- **CRUD Operations** for users
- **SQLAlchemy ORM** for database interactions
- **Data Validation** with Marshmallow
- **API Documentation** with Swagger UI
- **Containerization** with Docker

## Technologies Used ⚙️

- **Backend**: Python 3.12, Flask
- **Database**: SQLite (via SQLAlchemy)
- **Validation**: Marshmallow
- **Documentation**: Swagger UI
- **Linting**: Ruff
- **Testing**: Pytest
- **Containerization**: Docker, Docker Compose
- **Environment Management**: Poetry, Python-dotenv

---

## Getting Started 🐾

### Prerequisites

- Python 3.12+
- Poetry
- Docker and Docker Compose (optional)
- Make (optional)

### Local Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/dxrrkwm/flask-users.git
cd flask-users
```

#### 2. Install Dependencies
```bash
make deps
```
or
```bash
poetry install
```

#### 3. Run the Application
```bash
make run
```
or
```bash
poetry run flask run
```

The server will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

### Docker Setup 🐳

Build and start the service with Docker Compose:
```bash
make up-build
```
or
```bash
docker-compose up --build
```

The API will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Makefile Commands 🛠️

- `make deps`: Install dependencies using Poetry
- `make run`: Run the Flask development server
- `make up`: Start the Docker containers
- `make down`: Stop the Docker containers
- `make build`: Build the Docker image
- `make up-build`: Build and start the Docker containers
- `make test`: Run tests
- `make lint`: Run code linting with Ruff
- `make clean`: Remove cache files

---

## API Endpoints 🧩

Below is a list of the available API endpoints:

### Users
- `GET /users`: Get all users
- `POST /users`: Create a new user
- `GET /users/{id}`: Get a specific user
- `PUT /users/{id}`: Update a user
- `DELETE /users/{id}`: Delete a user

## API Documentation 📄

API documentation is available via Swagger UI at:
```
http://127.0.0.1:5000/api/docs
```
