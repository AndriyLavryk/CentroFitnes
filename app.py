from flask import Flask, render_template, redirect, url_for, request

from client import Client
from client_DAO import ClientDAO
from client_form import ClientForm
from connection import Connection  # Importa la clase con init_db()

import secrets


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app_title = 'Фитнес-центр '

@app.route('/')
@app.route('/index.html')
def home():
    app.logger.debug('Stepik, privet')
    clients_db = ClientDAO.select_all()
    client = Client()
    client_form = ClientForm(obj=client)
    return render_template('index.html', title=app_title,
                           clients=clients_db, form=client_form)

@app.route('/save', methods=['POST'])
def save():
    client = Client()
    client_form = ClientForm(obj=client)
    if client_form.validate_on_submit():
        client_form.populate_obj(client)
        if client.id:
            ClientDAO.update(client)
        else:
            ClientDAO.insert(client)
    return redirect(url_for('home'))

@app.route('/clear')
def clear():
    return redirect(url_for('home'))

@app.route('/edit/<int:id>')
def edit(id):
    client = ClientDAO.select_by_id(id)
    client_form = ClientForm(obj=client)
    clients_db = ClientDAO.select_all()
    return render_template('index.html', title=app_title,
                           clients=clients_db, form=client_form)

@app.route('/delete/<int:id>')
def delete(id):
    client_to_delete = ClientDAO.select_by_id(id)
    ClientDAO.delete(client_to_delete)
    return redirect(url_for('home'))

@app.route('/delete_multiple')
def delete_multiple():
    ids = request.args.get("ids")
    if ids:
        id_list = ids.split(",")
        for client_id in id_list:
            client_to_delete = ClientDAO.select_by_id(client_id)
            if client_to_delete:
                ClientDAO.delete(client_to_delete)
    return redirect(url_for('home'))

if __name__ == '__main__':
    Connection.init_db()  # Inicializa la BD y tabla si no existen
    app.run(debug=True)
