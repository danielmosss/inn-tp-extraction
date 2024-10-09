import sqlite3
import spacy
import os
import sys

# Load the spaCy model
nlp = spacy.load("en_core_web_trf")

# Function to process a book and store the results in the database
def process_book(book_id, db_name="books_with_genres.db"):
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Fetch the book text by book_id
    cursor.execute('SELECT book_id, text FROM books WHERE book_id = ?', (book_id,))
    book = cursor.fetchone()

    if not book:
        print(f"Book with ID {book_id} not found.")
        return

    book_id, text = book

    # Process the text with spaCy
    doc = nlp(text)

    # Create table for storing terms and categories if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book_terms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id TEXT,
            term TEXT,
            category TEXT,
            FOREIGN KEY (book_id) REFERENCES books(book_id)
        )
    ''')

    # Insert terms and categories into the database
    for ent in doc.ents:
        cursor.execute('''
            INSERT INTO book_terms (book_id, term, category)
            VALUES (?, ?, ?)
        ''', (book_id, ent.text, ent.label_))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print(f"Processed book with ID {book_id}.")

# Function to process all books or specific books by IDs
def process_books(book_ids=None, db_name="books_with_genres.db"):
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    if book_ids:
        # Process specific books by IDs
        for book_id in book_ids:
            process_book(book_id, db_name)
    else:
        # Process all books
        cursor.execute('SELECT book_id FROM books')
        all_books = cursor.fetchall()
        for book in all_books:
            process_book(book[0], db_name)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Process specific books by IDs
        book_ids = sys.argv[1:]
        process_books(book_ids)
    else:
        # Process all books
        process_books()