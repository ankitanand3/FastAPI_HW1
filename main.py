import models, database, schemas, crud
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List


Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependecy with db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# endpoints
# 1. add a book
@app.post('/book_add', response_model=schemas.BookOut)
def add_book(book: schemas.BookAdd, db: Session = Depends(get_db)):
    return crud.add_a_new_book(db, book)



# 2. Get a specific book by id
@app.get('/book/{book_id}', response_model=schemas.BookOut)
def specific_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_a_book_by_id(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail='Book not found')
    return book



# 3. Get all books
@app.get('/books', response_model=List[schemas.BookOut])
def get_books(db: Session = Depends(get_db)):
    return crud.get_all_books(db)


# 4. Get all book of this writer
@app.get('/book/{writer_name}', response_model=List[schemas.BookOut])
def get_books_by_writer_name(writer_name: str, db: Session = Depends(get_db)):
    books = crud.get_all_books_by_writer(db, writer_name)
    if books is None:
        raise HTTPException(status_code=404, detail=f'No books found for {writer_name} writer')
    return books


# 5. Get all books by year
@app.get('/book/{year}', response_model=List[schemas.BookOut])
def get_books_by_year(year: int, db: Session = Depends(get_db)):
    books = crud.get_book_by_year(db, year)
    if books is None:
        raise HTTPException(status_code=404, detail=f'No books found for {year}')
    return books



# 7. Change a book
@app.put('/book/{book_id}', response_model=schemas.BookOut)
def change_book(book_id: int, book: schemas.BookChange, db: Session = Depends(get_db)):
    db_book = crud.change_book(db, book_id, book)
    if db_book is None:
        raise HTTPException(status_code=404, detail='Book not found')
    return db_book

# 7. Delete a book
@app.delete('/books/{book_id}', response_model=dict)    
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_a_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail='Book not found')
    return {'detail': 'Book deleted'}