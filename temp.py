import sqlite3

connection = sqlite3.connect(r"Movies.db")

cursor = connection.cursor()
cursor.execute("DROP TAble if exists movies")
cursor.execute('''CREATE TABLE `movies`(
            `name` text,
            `lead_actor` text,
            `lead_actress` text,
            `release_year` int,
            `director` text
        )''')
connection.commit()

movie_data = ['Sooryavanshi', 'Akshay Kumar', 'Katrina Kaif', 2021, 'Rohit Shetty']
cursor.execute('''INSERT INTO `movies` (name, lead_actor, lead_actress, release_year, director) 
        VALUES (?, ?, ?, ?, ?)''', (movie_data[0], movie_data[1], movie_data[2], movie_data[3], movie_data[4]))
connection.commit()

movie_data = ['Bell Bottom', 'Akshay Kumar', 'Vaani Kapoor', 2021, 'Ranjit Tiwari']
cursor.execute('''INSERT INTO `movies` (name, lead_actor, lead_actress, release_year, director) 
        VALUES (?, ?, ?, ?, ?)''',(movie_data[0], movie_data[1], movie_data[2], movie_data[3], movie_data[4]))
connection.commit()

movie_data = ['Dangal', 'Aamir Khan', 'Sanya Malhotra', 2016, 'Nitesh Tiwari']
cursor.execute('''INSERT INTO `movies` (name, lead_actor, lead_actress, release_year, director) 
        VALUES (?, ?, ?, ?, ?)''',(movie_data[0], movie_data[1], movie_data[2], movie_data[3], movie_data[4]))
connection.commit()

cursor.execute('SELECT * FROM `movies`')
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute('SELECT * FROM movies WHERE lead_actor = ?', ("Akshay Kumar",))
result = cursor.fetchall()
for row in result:
    print(row[0])

connection.close()