from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository import contacts as repository_contacts
from src.schemas import ContactModel, ContactResponse

router = APIRouter(prefix='/contacts', tags=['contacts'])


# Create contact
@router.post('/create', response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    contact = await repository_contacts.create_contact(body, db)
    return contact


# Get all contacts
@router.get('/all', response_model=List[ContactResponse])
async def get_contacts(db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return contacts


# Get contact by id
@router.get('/{contact_id}', response_model=ContactResponse)
async def get_contact(contact_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contacts(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return contact


# Update contact

@router.put('/update/{contact_id}', response_model=ContactResponse)
async def update_contact(body: ContactModel, contact_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact(body, contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    return contact


# Delete contact
@router.delete("/delete/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_contact(contact_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.remove_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact
