from dataclasses import dataclass
from datetime import datetime

@dataclass
class DocumentExtract:
    expedition_date: datetime
    responsible_registry: str
    registration_number: str
    property_type: str 
    block: str 
    street: str 
    street_2: str
    property_number: str
    property_number_2: str 
    address_complement: str
    neighborhood: str
    city: str
    state: str
    property_footage: str
    owners_quantity: str
    owner_1: str
    owner_2: str 
    document_owner_1: str
    document_owner_2: str
    mortgage: str
    mortgage_owner_name: str
    mortgage_owner_document: str
    fiduciary_alienation: str
    fiduciary_alienation_owner_name: str
    fiduciary_alienation_owner_document: str
    garnishment: str