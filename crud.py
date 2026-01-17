# Functions for CRUD Operations
import models, schemas
from sqlalchemy.orm import Session, session

# get all books
def get_all_books(db: Session):
    return db.query(models.Books).all()


# get a specific book by id
def get_a_book_by_id(db: Session, book_id: int):
    return (
        db.query(models.Books).filter(models.Books.id == book_id).first()
    )



# get all the books by writer name
def get_all_books_by_writer(db: Session, writer_name: str):
    return (
        db.query(models.Books).filter(models.Books.Writer == writer_name).all()
    )




# get all the books by year
def get_book_by_year(db: Session, book_year: int):
    return (
        db.query(models.Books).filter(models.Books.Year == book_year).all()
    )


# add a new book
def add_a_new_book(db: Session, add_book: schemas.BookAdd):
    db_book = models.Books(Name=add_book.Name, Writer=add_book.Writer, Year=add_book.Year)
    if db_book:
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
    return db_book


# change_book
def change_book(db: Session, book_id: int, change_book: schemas.BookChange):
    db_book = db.query(models.Books).filter(models.Books.id == book_id).first()
    if db_book:
        db_book.Name = change_book.Name
        db_book.Writer = change_book.Writer
        db_book.Year = change_book.Year
        db.commit()
        db.refresh(db_book)
    return db_book



# delete a book
def delete_a_book(db: Session, book_id: int):
    db_book = db.query(models.Books).filter(models.Books.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book