import os
import json

# Function to extract book details from the input text
def extract_books_from_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    
    books_raw = data.split("\n")
    books = []
    print(f"Total books found: {len(books_raw)}")

    for book_raw in books_raw:
        if book_raw.strip():
            try:
                lines = book_raw.split("\t")
                book_id = lines[0]
                mid = lines[1]
                title = lines[2]
                author = lines[3]
                publication_date = lines[4]
                genres_dict = json.loads(lines[5])
                genres = list(genres_dict.values())
                text = "\t".join(lines[6:])

                book = {
                    "book_id": book_id,
                    "mid": mid,
                    "title": title,
                    "author": author,
                    "publication_date": publication_date,
                    "genres": genres,
                    "text": text
                }

                books.append(book)
            except (IndexError, json.JSONDecodeError) as e:
                print(f"Error processing: {book_raw} - {e}")
                continue
    return books

def write_books_to_json(books, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for book in books:
        # Create a file name using the book's title and author
        filename = f"{book['title'].replace(' ', '_')}-{book['author'].replace(' ', '_')}.json"
        file_path = os.path.join(output_dir, filename)

        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(book, json_file, ensure_ascii=False, indent=4)

        print(f"Saved {file_path}")

def process_books(input_file):
    output_dir = "./output_books"
    books = extract_books_from_text(input_file)
    write_books_to_json(books, output_dir)

if __name__ == "__main__":
    input_file = "books.txt"  # Replace with your .txt file path
    process_books(input_file)