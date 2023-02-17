from faker import Faker
from sqlalchemy.orm import Session

from src.database.db import SessionLocal
from src.database.models import Contact
from src.schemas import ContactModel

fake = Faker('uk_UA')
database = SessionLocal()


def create_contacts(data: ContactModel, db: Session = database):
    contact = Contact(**data.dict())
    # print(contact, db)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


if __name__ == '__main__':
    for _ in range(50):
        random_contact = ContactModel(
            name=fake.first_name(),
            surname=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            birthday=fake.date(),
            description=fake.text()
        )
        create_contacts(data=random_contact, db=database)
