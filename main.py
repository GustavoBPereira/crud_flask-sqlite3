from flask import Flask, render_template, url_for, redirect, request
from dao import LivroDao

app = Flask(__name__)
app.secret_key = 'phi'

conn = LivroDao('livros.db')

#create
#read
#update
#delete
@app.route('/')
def index():
	lista = conn.read_all()
	return render_template('index.html', lista=lista)

@app.route('/delete/<int:id>')
def delete(id):
	conn.delete(id)
	return redirect(url_for('index'))

@app.route('/create', methods=['GET', 'POST',])
def create():
	return render_template('create.html')

@app.route('/generate', methods=['POST',])
def generate():
	titulo  = request.form['titulo']
	autor   = request.form['autor']
	editora = request.form['editora']
	conn.create(titulo,autor,editora)
	return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
	lista = conn.read_one(id)
	return render_template('edit.html', lista=lista)

@app.route('/change', methods=['POST',])
def change():
	titulo  = str(request.form['titulo'])
	autor   = str(request.form['autor'])
	editora = str(request.form['editora'])
	id   	= str(request.form['id'])
	conn.update(id,titulo,autor,editora)
	return redirect(url_for('index'))
	
if __name__ == '__main__':
	app.run()
