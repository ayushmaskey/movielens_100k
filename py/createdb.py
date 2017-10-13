import sqlite3

conn = sqlite3.connect('movie.db')
c=conn.cursor()

# c.execute('''drop table links''')
# c.execute('''drop table movies''')
# c.execute('''drop table ratings''')
# c.execute('''drop table tags''')

c.execute('''create table links (movieID int, imdbID int, tmdbID int)''')
c.execute('''create table movies (movieID int, title char(100), genres char(50))''') 
c.execute('''create table ratings (userID int, movieID int, rating float, timestamp datetime)''')
c.execute('''create table tags (userID int, movieID int, tag char(50), timestamp datetime)''')

conn.close()