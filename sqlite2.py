import sqlite3
import csv

#to connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

#will create the database with the neccessary information
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    postnummer INTEGER,
    poststed TEXT,
    kommunenummer INTEGER,
    kommunenavn TEXT,
    kategori TEXT
)
''')


#file path of my file
filename = "C:\\Users\\yasch\\Downloads\\Postnummerregister-Excel(2).csv"

#function to insert data into database
def insert_data_from_csv(filename, start_row):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        #will skip to the second row based on the users input
        if start_row == 2:
            next(reader)

        for row in reader:
            try:
                cursor.execute('''
                INSERT INTO users (postnummer, poststed, kommunenummer, kommunenavn, kategori)
                VALUES (?, ?, ?, ?, ?)
                ''', (row['Postnummer'], row['Poststed'], row['Kommunenummer'], row['Kommunenavn'], row['Kategori']))
            except sqlite3.Error as e:
                print("Error inserting data:", e)
    conn.commit()
    print("Data inserted successfully.")

#input for the user
start_row = int(input("Enter the starting row (1 or 2): "))

#calls the function to insert the data into the database
insert_data_from_csv(filename, start_row)






