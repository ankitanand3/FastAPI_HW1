# Write class for all kinds of operations and data validation using pydantic

from pydantic import BaseModel, StrictInt, StrictStr


class BookBase(BaseModel):
    id: StrictInt
    Name: StrictStr
    Writer: StrictStr
    Year: StrictInt

class BookAdd(BookBase):
    pass

class BookChange(BookBase):
    pass

class BookOut(BookBase):
    id: StrictInt

    class Config:
        orm_mode = True