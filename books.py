from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
  {"title": "Book One", "author": "Author One", "category": "science" },
  {"title": "Book Two", "author": "Author Two", "category": "economic"},
  {"title": "Book Three", "author": "Author Three","category": "philosophy"},
  {"title": "Book Four", "author": "Author Four", "category": "physic"},
  {"title": "Book Five", "author": "Author Five", "category": "math"},
  {"title": "Book Six", "author": "Author Two", "category": "math"},
]

@app.get("/books")
async def read_all_books():
  return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
  for book in BOOKS:
    if book.get("title").casefold() == book_title.casefold():
      return book
  return {"detail": "Book not found"}

@app.get("/books/")
async def read_category_by_query(category: str):
  books_to_return = []
  for book in BOOKS:
    if book.get("category").casefold() == category.casefold():
      books_to_return.append(book)
  return books_to_return

@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
  book_to_return = []
  for book in BOOKS:
    if book.get("author").casefold() == author.casefold():
      book_to_return.append(book)
  return book_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
  book_to_return = []
  for book in BOOKS:
    if book.get("author").casefold() == book_author.casefold() and \
        book.get("category").casefold() == category.casefold():
      book_to_return.append(book)
  return book_to_return

@app.post("/books/create_book")
async def create_book(new_book = Body()):
  BOOKS.append(new_book)
  return {"detail": "Book created successfully"}

@app.put("/books/update_book")
async def update_book(update_book = Body()):
  for i in range(len(BOOKS)):
    if BOOKS[i].get("title").casefold() == update_book.get("title").casefold():
      BOOKS[i] = update_book
  return {"detail": "Book updated successfully"}

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
  for i in range(len(BOOKS)):
    if BOOKS[i].get("title").casefold() == book_title.casefold():
      BOOKS.pop(i)
      return {"detail": "Book deleted successfully"}
  return {"detail": "Book not found"}