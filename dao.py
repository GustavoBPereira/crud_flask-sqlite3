import sqlite3

class LivroDao():

    def __init__(self, db):
        self.db = db

    def read_all(self):
        conn   = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM livros ORDER BY titulo,autor,editora,id')
        lista = cursor.fetchall()
        conn.close()
        return lista

    def create(self, titulo, autor, editora):
        conn   = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO livros(titulo,autor,editora) VALUES(?,?,?)',(titulo,autor,editora))
        conn.commit()
        conn.close()
        return True

    def read_one(self, id):
        conn   = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM livros WHERE id=?',(id,))
        resultado  = cursor.fetchone()
        conn.close()
        return resultado

    def update(self ,id ,titulo, autor, editora):
        conn   = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('UPDATE livros SET titulo=?, autor=?, editora=? WHERE id=?', (titulo,autor,editora,id))
        conn.commit()
        conn.close()
        return True

    def delete(self, id):
        conn   = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM livros WHERE id=?', (id,))
        conn.commit()
        conn.close()
        return True
    