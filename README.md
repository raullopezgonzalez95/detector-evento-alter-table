# detector-evento-alter-table

Script de Monitoreo de Eventos de ALTER TABLE

Este script está diseñado para monitorear eventos de modificación de tablas (ALTER TABLE) en una base de datos MySQL utilizando la biblioteca pymysqlreplication. Cuando se detecta un evento de ALTER TABLE en la base de datos especificada, el script imprime información relevante sobre el evento y la descripción de la tabla modificada.

Requisitos

Antes de ejecutar este script, asegúrate de tener instalada la biblioteca pymysqlreplication. Puedes instalarla utilizando el siguiente comando:

bash
Copy code
pip install pymysqlreplication
Cómo funciona

Importación de bibliotecas necesarias:
pymysqlreplication: Proporciona la funcionalidad para leer el registro binario de MySQL y capturar eventos.
pymysql: Se utiliza para establecer la conexión con la base de datos MySQL.
re: Se utiliza para buscar patrones en las consultas SQL.
Definición de la función process_alter_table(event, connection):
Esta función procesa un evento de tipo QueryEvent (evento de consulta SQL) en busca de sentencias ALTER TABLE.
Si se encuentra una sentencia ALTER TABLE, se extrae información relevante como el nombre de la base de datos, el nombre de la tabla y la descripción de la tabla modificada.
Utiliza una expresión regular para buscar la sentencia ALTER TABLE en la consulta SQL.
Configuración de la conexión a la base de datos MySQL:
Se definen los parámetros de conexión en el diccionario config, incluyendo el host, el puerto, el usuario, la contraseña y la base de datos.
Establecimiento de la conexión con la base de datos:
Se utiliza el diccionario config para establecer la conexión con la base de datos MySQL.
Creación de un BinLogStreamReader:
Se crea una instancia de BinLogStreamReader con los parámetros de conexión y el ID del servidor.
Se especifica que solo se deben capturar eventos de tipo QueryEvent.
Bucle de lectura de eventos:
El script entra en un bucle en el que lee los eventos del registro binario uno por uno.
Si el evento es de tipo QueryEvent, se llama a la función process_alter_table para analizar y mostrar información sobre el evento de ALTER TABLE.
Cierre de la transmisión y la conexión:
Una vez que se han procesado todos los eventos, se cierran tanto la transmisión de eventos como la conexión a la base de datos.
Uso

Asegúrate de que la biblioteca pymysqlreplication esté instalada.
Modifica los valores en el diccionario config para que coincidan con la configuración de tu base de datos.
Ejecuta el script.
El script se ejecutará en un bucle, monitoreando los eventos de ALTER TABLE en la base de datos. Cuando se detecte un evento, mostrará información sobre la base de datos, la tabla y la descripción de los cambios realizados.
Nota: Este script está diseñado para fines educativos y de monitoreo. Asegúrate de que tienes permisos adecuados en la base de datos antes de ejecutarlo en un entorno de producción.