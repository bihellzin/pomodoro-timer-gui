from db import Database


banco = Database()

banco.check_db()

banco.update(2, ['20', '4'])

banco.check_db()
