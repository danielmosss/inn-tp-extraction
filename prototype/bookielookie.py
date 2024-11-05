import sqlite3

def get_category(cursor):
    """
    Prompts the user to select a category from the distinct categories in the book_terms table.

    Args:
        cursor (sqlite3.Cursor): The SQLite cursor object.

    Returns:
        str: The selected category.
    """
    cursor.execute('SELECT DISTINCT category FROM book_terms')
    categories = cursor.fetchall()

    print("Choose a category:")
    for i, category in enumerate(categories):
        print(f"{i + 1}. {category[0]}")

    choice = int(input("Enter the category number: ")) - 1
    return categories[choice][0]


def get_search_term():
    return input("Enter the search term: ")


def fetch_records(cursor, category, search_term, offset, limit=10):
    """
    Fetches records from the book_terms table based on the category and search term, with pagination.

    Args:
        cursor (sqlite3.Cursor): The SQLite cursor object.
        category (str): The category to filter by.
        search_term (str): The search term to filter by.
        offset (int): The offset for pagination.
        limit (int, optional): The number of records to fetch per page. Defaults to 10.

    Returns:
        list: A list of tuples containing book_id, category, and concatenated terms.
    """
    cursor.execute('''
        SELECT book_id, category, GROUP_CONCAT(term, ', ') as terms
        FROM book_terms
        WHERE category = ? AND term LIKE ?
        GROUP BY book_id, category
        LIMIT ? OFFSET ?
    ''', (category, f'%{search_term}%', limit, offset))
    return cursor.fetchall()


def count_records(cursor, category, search_term):
    """
    Counts the total number of distinct book_ids in the book_terms table based on the category and search term.

    Args:
        cursor (sqlite3.Cursor): The SQLite cursor object.
        category (str): The category to filter by.
        search_term (str): The search term to filter by.

    Returns:
        int: The total number of distinct book_ids.
    """
    cursor.execute('''
        SELECT COUNT(DISTINCT book_id)
        FROM book_terms
        WHERE category = ? AND term LIKE ?
    ''', (category, f'%{search_term}%'))
    return cursor.fetchone()[0]


def main():
    """
    Main function to run the script. Connects to the SQLite database, prompts the user for category and search term,
    and displays the results with pagination.
    """

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
            book_id, category, terms = record
            print(f"Book ID: {book_id}, Category: {category}, Terms: [{terms}]")

        print(f"Showing books {offset + 1} to {min(offset + 10, total_records)} of {total_records}")

        offset += 10
        if offset < total_records:
            next_page = input("Next page = Enter, Quit = Q: ")
            if next_page.lower() == 'q':
                break

    conn.close()


if __name__ == "__main__":
    main()