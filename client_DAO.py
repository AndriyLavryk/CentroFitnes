from connection import Connection
from client import Client

class ClientDAO:
    SELECT_ALL = 'SELECT * FROM clients ORDER BY id'
    SELECT_BY_ID = 'SELECT * FROM clients WHERE id=?'
    INSERT = 'INSERT INTO clients(first_name, last_name, membership) VALUES(?, ?, ?)'
    UPDATE = 'UPDATE clients SET first_name=?, last_name=?, membership=? WHERE id=?'
    DELETE = 'DELETE FROM clients WHERE id=?'

    @classmethod
    def select_all(cls):
        connection = None
        try:
            connection = Connection.get_connection()
            cursor = connection.cursor()
            cursor.execute(cls.SELECT_ALL)
            records = cursor.fetchall()
            clients = [Client(*record) for record in records]
            return clients
        except Exception as e:
            print(f'Error al seleccionar todos los clientes: {e}')
        finally:
            if connection:
                cursor.close()
                Connection.release_connection(connection)

    @classmethod
    def insert(cls, client):
        connection = None
        try:
            connection = Connection.get_connection()
            cursor = connection.cursor()
            values = (client.first_name, client.last_name, client.membership)
            cursor.execute(cls.INSERT, values)
            connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al insertar cliente: {e}')
        finally:
            if connection:
                cursor.close()
                Connection.release_connection(connection)

    @classmethod
    def update(cls, client):
        connection = None
        try:
            connection = Connection.get_connection()
            cursor = connection.cursor()
            values = (client.first_name, client.last_name, client.membership, client.id)
            cursor.execute(cls.UPDATE, values)
            connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al actualizar cliente: {e}')
        finally:
            if connection:
                cursor.close()
                Connection.release_connection(connection)

    @classmethod
    def select_by_id(cls, client_id):
        connection = None
        try:
            connection = Connection.get_connection()
            cursor = connection.cursor()
            cursor.execute(cls.SELECT_BY_ID, (client_id,))
            record = cursor.fetchone()
            return Client(*record) if record else None
        except Exception as e:
            print(f'Error al seleccionar cliente por ID: {e}')
        finally:
            if connection:
                cursor.close()
                Connection.release_connection(connection)

    @classmethod
    def delete(cls, client):
        connection = None
        try:
            connection = Connection.get_connection()
            cursor = connection.cursor()
            cursor.execute(cls.DELETE, (client.id,))
            connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al eliminar cliente: {e}')
        finally:
            if connection:
                cursor.close()
                Connection.release_connection(connection)


if __name__ == '__main__':
    Connection.init_db()  # Asegura que la tabla exista

    new_client = Client(first_name="Alejandra", last_name='Lopez', membership=300)
    inserted_rows = ClientDAO.insert(new_client)
    print(f"Insertados: {inserted_rows}")

    client_to_update = Client(1, 'Alejandra', last_name='Lopez Fernandez', membership=400)
    updated_rows = ClientDAO.update(client_to_update)
    print(f"Actualizados: {updated_rows}")

    client_to_insert = Client(first_name='Andriy', last_name='Lavryk Sanchez', membership=23)
    inserted_rows = ClientDAO.insert(client_to_insert)
    print(f"Insertados: {inserted_rows}")

    client_to_delete = Client(id=1)
    deleted_rows = ClientDAO.delete(client_to_delete)
    print(f'Eliminados: {deleted_rows}')

    clients = ClientDAO.select_all()
    for client in clients:
        print(client)
