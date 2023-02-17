from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository import contacts as repository_contacts
from src.schemas import ContactModel, ContactResponse

router = APIRouter(prefix='/contacts', tags=['contacts'])
