import sqlite3


class Database:
  def __init__(self):
    self.conection = sqlite3.connect('profiles.db')
    self.cursor = self.conection.cursor()

    self.cursor.execute('CREATE TABLE IF NOT EXISTS profiles(id INTEGER PRIMARY KEY, \
        concentration text, \
        short_break text)'
    )

    self.conection.commit()


  def add(self, data: list):
    self.cursor.execute(
      'INSERT INTO profiles VALUES(NULL, ?, ?) \
    ', (data[0], data[1]))

    self.conection.commit()


  def check_db(self):
    self.cursor.execute('SELECT * FROM profiles')

    result = self.cursor.fetchall()
    
    print(result)

    self.conection.commit()
  

  def remove(self, id: int):
    self.cursor.execute('DELETE FROM profiles WHERE id=?', (id,))
    self.conection.commit()
  

  def update(self, id: int, data: list):
    self.cursor.execute("UPDATE profiles SET concentration = ?, short_break = ? \
    WHERE id = ?", (data[0], data[1], id))

    self.conection.commit()