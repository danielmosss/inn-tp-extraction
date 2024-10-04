## get books from ../preprocess_books/output_books_github/ and put them in a sqlite database
## Every book file is an json file with the following structure:
#{
#     "book_id": "1282996",
#     "mid": "/m/02p43y5",
#     "title": "\"A\" is for Alibi",
#     "author": "Sue Grafton",
#     "publication_date": "1982-04-15",
#     "genres": [
#         "Mystery",
#         "Speculative fiction",
#         "Fiction",
#         "Suspense"
#     ],
#     "text": " The first novel in the \"Alphabet Mysteries\" series introduces the character of Kinsey Millhone as she looks into through the facts surrounding the death of prominent divorce lawyer Laurence Fife, whose murder eight years previously was blamed on his wife, Nikki Fife. After being released from prison, Nikki hires Kinsey to find the true murderer. In the course of the investigation, Kinsey becomes involved with Charlie Scorsoni, Laurence's former business partner, whose charms are sufficient to overcome temporarily Kinsey's reservations about sleeping with someone she hasn't yet crossed off her list of suspects. While flipping through the police reports courtesy (somewhat belligerently) of Lieutenant Dolan, Kinsey discovers something which never came up at Nikki's trial: that Laurence's death has been linked by police to that of an accountant in Los Angeles, Libby Glass. Both died under the same circumstances - oleander capsules were substituted for allergy pills - and Kinsey soon learns that the two were rumoured to be having an affair. She tracks down Libby's parents, and meets Libby's former boyfriend, Lyle, whom she suspects of being involved in Libby's death. Kinsey interrupts someone meddling with the boxes of Libby's possessions in the Glasses' basement, and on searching through what remains, finds nothing of significance except a letter from Laurence, indicating that he was in love with 'Elizabeth', which seems to confirm that he and Libby were indeed having an affair. Kinsey goes to Las Vegas on the track of Laurence's ex-secretary, Sharon Napier, who apparently had a mysterious hold over Laurence, but Sharon is shot minutes before Kinsey arrives on the scene to interview her, and Kinsey has to get out fast before she is caught in a compromising situation. It seems that like with the boxes in the basement, someone else is just ahead of her. Back in California, and quizzing Nikki further, Kinsey is mystified that Nikki's young son, Colin, recognises Laurence's first wife, Gwen, in a photograph. Kinsey has already discovered from a couple of interviews with her that Gwen is very bitter about her break-up with Laurence, but the only way that Gwen could have come into contact with Colin would have been through Laurence. Kinsey surmises that despite Gwen's hatred of Laurence, they were having an affair at the time of his death, and when she accuses Gwen of this, Gwen finally confesses - not only to the affair but to murdering Laurence. Shortly afterwards, she too is dead: killed in a hit and run accident. Kinsey has solved the case she was hired to solve, but the knowledge of Gwen's affair with Laurence leads her to question her previous assumption that he was involved with Libby Glass. She realises the letter in Libby's belongings was a plant - dating from an affair with Sharon Napier's mother, Elizabeth, many years before. So who killed Libby? In a plot twist, she discovers that her previous notions about Libby's death were entirely wrong: In fact, it was Charlie Scorsoni who had been having an affair with Libby, and he killed her when she discovered he was embezzling money from mutual accounts. He'd used the same method as Gwen used to kill Laurence only a few days before as a cover for her murder, so that everyone would assume the same person was guilty of both murders. Charlie realises that Kinsey has worked out the truth, and during a dramatic confrontation, he pursues her across the beach, armed with a knife. Before he can kill her, she shoots him dead instead. The novel ends as it begins, with Kinsey, exonerated as acting in self-defence, reflecting on the experience of having killed someone."
# }

# now make a function that will create an sqlite database with al this information. 



import sqlite3
import json
import os

# Updating the path to point to the correct directory and adding a separate table for genres
books_dir = "./books"

# Function to create and populate the SQLite database with an additional genres table
def create_books_database_with_genres(db_name="books_with_genres.db"):
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table for books
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id TEXT PRIMARY KEY,
            mid TEXT,
            title TEXT,
            author TEXT,
            publication_date TEXT,
            text TEXT
        )
    ''')

    # Create table for genres
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS genres (
            genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id TEXT,
            genre TEXT,
            FOREIGN KEY (book_id) REFERENCES books(book_id)
        )
    ''')

    # Read all book files from the directory
    for file_name in os.listdir(books_dir):
        if file_name.endswith(".json"):
            file_path = os.path.join(books_dir, file_name)

            # Load the JSON content
            with open(file_path, 'r', encoding='utf-8') as f:
                book_data = json.load(f)
                # Prepare data for insertion into the books table
                book_id = book_data["book_id"]
                mid = book_data["mid"]
                title = book_data["title"]
                author = book_data["author"]
                publication_date = book_data["publication_date"]
                text = book_data["text"]

                # Insert data into the books table
                cursor.execute('''
                    INSERT OR REPLACE INTO books (book_id, mid, title, author, publication_date, text)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (book_id, mid, title, author, publication_date, text))

                # Insert genres into the genres table
                for genre in book_data["genres"]:
                    cursor.execute('''
                        INSERT INTO genres (book_id, genre)
                        VALUES (?, ?)
                    ''', (book_id, genre))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to get a random book along with its genres
def get_random_book_with_genres(db_name="books_with_genres.db"):
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Fetch a random book
    cursor.execute('''
        SELECT b.book_id, b.mid, b.title, b.author, b.publication_date, b.text, 
               GROUP_CONCAT(g.genre, ', ') AS genres
        FROM books b
        LEFT JOIN genres g ON b.book_id = g.book_id
        GROUP BY b.book_id
        ORDER BY RANDOM() LIMIT 1
    ''')

    # Fetch and display the result
    random_book = cursor.fetchone()

    # Close the connection
    conn.close()

    if random_book:
        return {
            "book_id": random_book[0],
            "mid": random_book[1],
            "title": random_book[2],
            "author": random_book[3],
            "publication_date": random_book[4],
            "text": random_book[5],
            "genres": random_book[6]
        }
    else:
        return None

print("Do you want to create the database? (y/n)")
response = input()
if response.lower() == "y":
    create_books_database_with_genres()
    print("Database created successfully!")
else:
    print("Database not created.")

# Fetch a random book with all its information
random_book_info = get_random_book_with_genres()
print(random_book_info)

