import sqlite3

def create_db():
  conection = sqlite3.connect('profiles.db')
  cursor = conection.cursor()

  cursor.execute('''
    create table profiles(
      concentration text,
      short_break text)
  ''')

  conection.commit()
  cursor.close()
  conection.close()


def add_to_db(data: list):
  conection = sqlite3.connect('profiles.db')
  cursor = conection.cursor()

  cursor.execute('''
    insert into profiles (concentration, short_break)
    values(?, ?)
  ''', (data[0], data[1]))

  conection.commit()
  cursor.close()
  conection.close()


def check_db():
  conection = sqlite3.connect('profiles.db')
  cursor = conection.cursor()

  cursor.execute('select * from profiles')

  result = cursor.fetchone()
  
  print(result)

  conection.commit()
  cursor.close()
  conection.close()