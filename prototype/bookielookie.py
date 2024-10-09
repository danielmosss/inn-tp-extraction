import sqlite3
import os


def get_category(cursor):
    cursor.execute('SELECT DISTINCT category FROM book_terms')
    categories = cursor.fetchall()

    print("Choose a category:")
    for i, category in enumerate(categories):
        print(f"{i + 1}. {category[0]}")

    choice = int(input("Enter the category number: ")) - 1
    return categories[choice][0]


def get_search_term():
    return input("Enter the search term: ")


def fetch_records(cursor, category, search_term, offset, limit=20):
    cursor.execute('''
        SELECT book_id, term, category 
        FROM book_terms 
        WHERE category = ? AND term LIKE ? 
        LIMIT ? OFFSET ?
    ''', (category, f'%{search_term}%', limit, offset))
    return cursor.fetchall()


def count_records(cursor, category, search_term):
    cursor.execute('''
        SELECT COUNT(*) 
        FROM book_terms 
        WHERE category = ? AND term LIKE ?
    ''', (category, f'%{search_term}%'))
    return cursor.fetchone()[0]


def main():
    db_name = "books_with_genres.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    category = get_category(cursor)
    search_term = get_search_term()

    total_records = count_records(cursor, category, search_term)
    print(f"Total records found: {total_records}")

    offset = 0
    while offset < total_records:
        records = fetch_records(cursor, category, search_term, offset)
        for record in records:
            print(record)

        offset += 20
        if offset < total_records:
            next_page = input("Press Enter to see the next page or type 'q' to quit: ")
            if next_page.lower() == 'q':
                break

    conn.close()


if __name__ == "__main__":
    main()