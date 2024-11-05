In this directory you will find the following files and folders:

- 'books' is a folder that holds books per file in .json file format.
   These books came from preprocessing_books directory. Check [README.md](../preprocess_books/README.md)
- create_and_insert_book_into_database.py is the first script you need to run.
   This will create a database and insert all the books from ./books into the database. 
- process_books_to_db.py is a script that processes the books with NLP and inserts the results into the database.
- bookielookie.py is the main application. This is the searchengine that will be used to search for books in the database that have been processed.

## How to run the app
1. Run the script `create_and_insert_book_into_database.py`
2. Run the script `process_books_to_db.py`
3. Run the script `bookielookie.py`