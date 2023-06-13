import React from 'react'
import "../CSS/book.css"

function Book(book) {
  return (
    <div className = "Book">
        <div className="book-photo">
            <img src={book.photo} alt="" />
        </div>
        <div className="book-info">
            <h1 className="book-title">
                {book.title}
            </h1>

            <div className="book-author">
                {book.author}
            </div>


        </div>
    </div>
  )
}

export default Book