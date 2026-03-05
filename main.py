from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

import models
import schemas
import crud
from database import SessionLocal, engine
from utils import calculate_distance


# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses/", response_model=schemas.AddressResponse)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    logger.info("Creating new address")
    return crud.create_address(db, address)


@app.get("/addresses/", response_model=list[schemas.AddressResponse])
def list_addresses(db: Session = Depends(get_db)):
    return crud.get_addresses(db)


@app.put("/addresses/{address_id}", response_model=schemas.AddressResponse)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    updated = crud.update_address(db, address_id, address)
    if not updated:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated


@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_address(db, address_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Address deleted successfully"}


@app.get("/addresses/nearby/")
def get_nearby_addresses(latitude: float, longitude: float, distance_km: float,
                         db: Session = Depends(get_db)):
    all_addresses = crud.get_addresses(db)
    nearby = []

    for addr in all_addresses:
        dist = calculate_distance(latitude, longitude, addr.latitude, addr.longitude)
        if dist <= distance_km:
            nearby.append(addr)

    return nearby