from typing import Optional
from sqlmodel import SQLModel, select, Field
from pydantic import validator
from statistics import mean
from datetime import datetime


class Beer (SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=True, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    date: datetime = Field(default_factory=datetime.now)

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    @validator("rate", always=True, check_fields=False)
    def calculate_rate(cls, v, values):
        rate = mean(
            [
                values['flavor'], 
                values['image'], 
                values['cost']
            ]
        )
        return int(rate)
 
brewdog = Beer(name='Brahma', style='Ruim', flavor=6, image=6, cost=9)