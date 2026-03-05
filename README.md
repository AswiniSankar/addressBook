# Address Book API

A simple **Address Book REST API** built using **FastAPI**, **SQLAlchemy**, and **SQLite**.  
This API allows users to store, update, delete, and retrieve address records and also find nearby addresses based on geographic coordinates.

---

## Features

- Create a new address
- View all saved addresses
- Update an existing address
- Delete an address
- Find nearby addresses using **latitude and longitude**
- SQLite database integration
- Logging support
- RESTful API design

---

## Tech Stack

- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Uvicorn**

---

## Project Structure

```
AddressBook/
│
├── main.py          # FastAPI application and API endpoints
├── database.py      # Database connection setup
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── crud.py          # Database operations
├── utils.py         # Utility functions (distance calculation)
└── requirement.txt  # Install the requirements

```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AswiniSankar/addressBook
```

### 2. Create Virtual Environment

```bash
python3 -m venv .env
source .env/bin/activate
```

### 3. Install Dependencies

```bash
pip3 install fastapi uvicorn sqlalchemy
```
or run a below command

```bash
pip3 install -r requirement.txt
```


---

## Running the Application

Start the FastAPI server using **Uvicorn**:

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates API documentation.

Swagger UI:
```
http://127.0.0.1:8000/docs
```

Alternative documentation:
```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Create Address

**POST**

```
/addresses/
```

Example request body:

```json
{
  "name": "John Doe",
  "street": "123 Main St",
  "city": "New York",
  "latitude": 40.7128,
  "longitude": -74.0060
}
```

---

### Get All Addresses

**GET**

```
/addresses/
```

---

### Update Address

**PUT**

```
/addresses/{address_id}
```

---

### Delete Address

**DELETE**

```
/addresses/{address_id}
```

---

### Find Nearby Addresses

**GET**

```
/addresses/nearby/?latitude=12.9716&longitude=77.5946&distance_km=5
```

Returns addresses within the given distance.

---

## Database

The project uses **SQLite** for simplicity.

The database file (`address.db`) is created automatically when the application runs.

---

## Future Improvements

- Add authentication
- Add pagination
- Add unit tests
- Deploy using Docker
- Add PostgreSQL support

---
