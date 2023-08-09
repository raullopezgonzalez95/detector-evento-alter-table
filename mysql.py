from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.event import QueryEvent
import pymysql
import re
import time

def process_alter_table(event, connection):
    query = event.query.lower()
    if "alter table" in query:
        print("Se detectó un evento de ALTER TABLE:")
        print(f"Base de datos: {event.schema}")
        print(f"Sentencia: {event.query}")

        match = re.search(r'alter table (\w+(?:\.\w+)?)', query)
        if match:
            database_table = match.group(1)
            if '.' in database_table:
                database, table = database_table.split('.')
            else:
                database = None
                table = database_table
            
            print(f"Tabla: {table}")

            if database:
                describe_query = f"DESCRIBE {database}.{table};"
            else:
                describe_query = f"DESCRIBE {table};"
        
        with connection.cursor() as cursor:
            cursor.execute(describe_query)
            description = cursor.fetchall()
            print("Descripción de la tabla modificada:")
            for column_info in description:
                print(column_info)
        
        return True

config = {
    'host': 'localhost',
    'port': 3307,
    'user': 'root',
    'passwd': 'my-secret-pw',
    'db': 'db_name'
}

connection = pymysql.connect(
    host=config['host'],
    port=config['port'],
    user=config['user'],
    password=config['passwd'],
    database=config['db'],
    autocommit=True
)

stream = BinLogStreamReader(
    connection_settings=config,
    server_id=100,
    only_events=[QueryEvent])

for binlogevent in stream:
    if isinstance(binlogevent, QueryEvent):
        process_alter_table(binlogevent, connection)

stream.close()
connection.close()
